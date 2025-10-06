'''
Synchronous or Asynchronous Endpoint using httpx
================================================

This endpoint implements GraphQL client using the :mod:`httpx` library.


This module provides command line utility:

.. code-block:: console

   $ python3 -m sgqlc.endpoint.httpx http://server.com/ '{ queryHere { ... } }'

It's pretty much like :class:`sgqlc.endpoint.http.HTTPEndpoint`, but
using the :mod:`httpx`. This allows you to make asynchronous requests using
:mod:`httpx.AsyncClient` or re-using a global client for better connection
pooling.

Example using :class:`sgqlc.endpoint.httpx.HTTPXEndpoint`:

.. literalinclude:: ../../examples/basic/04_httpx_endpoint.py
   :language: python

The ``query`` may be given as ``bytes`` or ``str`` as in the example, but
it may be a :class:`sgqlc.operation.Operation`, which will serialize as
string while also providing convenience to interepret the results.

See `more examples <https://github.com/profusion/sgqlc/tree/master/examples>`_.

:license: ISC
'''

__docformat__ = 'reStructuredText en'

__all__ = ('HTTPXEndpoint',)

import json
import httpx

from .base import add_query_to_url
from .http import HTTPEndpoint
from typing import Optional, Union, Dict


class HTTPXEndpoint(HTTPEndpoint):
    '''GraphQL endpoint access via httpx.

    This helper is very thin, just setups the correct HTTP request to
    GraphQL endpoint, handling logging of HTTP and GraphQL errors. The
    object is callable with parameters: ``query``, ``variables``,
    ``operation_name``, ``extra_headers`` and ``timeout``.

    The user of this class should create GraphQL queries and interpret the
    resulting object, created from JSON data, with top level properties:

    :data: object matching the GraphQL requests, or ``null`` if only
       errors were returned.

    :headers: dictionary of HTTP response headers.

    :errors: list of errors, which are objects with the key "message" and
       optionally others, such as "location" (for errors matching GraphQL
       input). Instead of raising exceptions, such as
       :exc:`requests.exceptions.HTTPError` or
       :exc:`json.JSONDecodeError` those are stored in the
       "exception" key.

    :client: The httpx.Client() or httpx.AsyncClient(). If you are using an
       AsyncClient, the endpoint call will return a coroutine you can await.

    .. note::

      Both ``data`` and ``errors`` may be returned, for instance if
      a null-able field fails, it will be returned as null (Python
      ``None``) in data the associated error in the array.

    The class has its own :class:`logging.Logger` which is used to
    debug, info, warning and errors. Error logging and conversion to
    uniform data structure similar to GraphQL, with ``{"errors": [...]}``
    is done by :func:`HTTPXEndpoint._log_httpx_error()` own method,
    ``BaseEndpoint._log_json_error()`` and
    ``BaseEndpoint._log_graphql_error()``. This last one will show the
    snippets of GraphQL that failed execution.

    '''

    def __init__(
        self,
        *args,
        client: Optional[httpx.Client] = None,
        **kwargs,
    ):
        '''
        :param client: The existing httpx.Client to use.
        :type client: httpx.Client
        '''
        super().__init__(*args, **kwargs)
        self.client = client or httpx.Client()

    def __call__(
        self,
        query: Union[bytes, str],
        variables: Optional[Dict] = None,
        operation_name: Optional[str] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[int] = None,
    ):
        '''Calls the GraphQL endpoint.

        :param query: the GraphQL query or mutation to execute. Note
          that this is converted using ``bytes()``, thus one may pass
          an object implementing ``__bytes__()`` method to return the
          query, eventually in more compact form (no indentation, etc).
        :type query: :class:`str` or :class:`bytes`.

        :param variables: variables (dict) to use with
          ``query``. This is only useful if the query or
          mutation contains ``$variableName``.
        :type variables: dict

        :param operation_name: if more than one operation is listed in
          ``query``, then it should specify the one to be executed.
        :type operation_name: str

        :param extra_headers: dict with extra HTTP headers to use.
        :type extra_headers: dict

        :param timeout: overrides the default timeout.
        :type timeout: float

        :return: dict with optional fields ``data`` containing the GraphQL
          returned data as nested dict, ``headers`` with a dictionary of
          response headers, and ``errors`` with an array of errors.
          Note that both ``data`` and ``errors`` may be returned!
        :rtype: dict

        '''
        query, req = self._prepare(
            query=query,
            variables=variables,
            operation_name=operation_name,
            extra_headers=extra_headers,
        )

        req.extensions['timeout'] = httpx.Timeout(
            timeout or self.timeout
        ).as_dict()

        if isinstance(self.client, httpx.AsyncClient):

            async def runner():
                try:
                    response = await self.client.send(req)
                    return self._parse_httpx_response(query, response)
                except httpx.HTTPError as exc:
                    return self._log_httpx_error(query, req, exc)

            return runner()
        elif isinstance(self.client, httpx.Client):
            try:
                response = self.client.send(req)
                return self._parse_httpx_response(query, response)
            except httpx.HTTPStatusError as exc:
                return self._log_httpx_error(query, req, exc)

    def _parse_httpx_response(self, query, response):
        response.raise_for_status()

        try:
            data = response.json()
            if data and data.get('errors'):
                return self._log_graphql_error(query, data)
            return data
        except json.JSONDecodeError as exc:
            return self._log_json_error(response.text, exc)

    def _log_httpx_error(self, query, request, exc):
        self.logger.error('%s: %s', request.url, exc)

        content_type = exc.response.headers.get('Content-Type', '')
        body = exc.response.text
        if not content_type.startswith('application/json'):
            return {
                'data': None,
                'errors': [
                    {
                        'message': str(exc),
                        'exception': exc,
                        'status': exc.response.status_code,
                        'headers': dict(exc.response.headers),
                        'body': body,
                    }
                ],
            }
        else:
            # GraphQL servers return 400 and {'errors': [...]}
            # if only errors was returned, no {'data': ...}

            try:
                data = exc.response.json()
            except json.JSONDecodeError as exc:
                return self._log_json_error(body, exc)

            if isinstance(data, dict) and data.get('errors'):
                data.update(
                    {
                        'exception': exc,
                        'status': exc.response.status_code,
                        'headers': dict(exc.response.headers),
                    }
                )
                return self._log_graphql_error(query, data)

            return {
                'data': None,
                'errors': [
                    {
                        'message': str(exc),
                        'exception': exc,
                        'status': exc.response.status_code,
                        'headers': dict(exc.response.headers),
                        'body': body,
                    }
                ],
            }

    def get_http_post_request(self, query, variables, operation_name, headers):
        '''Create an HTTP POST request for the query.'''
        return self.client.build_request(
            method='POST',
            url=self.url,
            headers=headers,
            json={
                'query': query,
                'variables': variables,
                'operationName': operation_name,
            },
        )

    def get_http_get_request(self, query, variables, operation_name, headers):
        '''Create an HTTP GET request for the query.'''
        params = {'query': query}
        if operation_name:
            params['operationName'] = operation_name

        if variables:
            params['variables'] = json.dumps(variables)

        url = add_query_to_url(self.url, params)

        return self.client.build_request(
            method='GET', url=url, headers=headers
        )
