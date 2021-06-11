'''
Synchronous HTTP Endpoint using python-requests
===============================================

This endpoint implements GraphQL client using the :mod:`requests` library.

This module provides command line utility:

.. code-block:: console

   $ python3 -m sgqlc.endpoint.requests http://server.com/ '{ query { ... } }'

It's pretty much like :class:`sgqlc.endpoint.http.HTTPEndpoint`, but
using the :mod:`requests`. This comes with the convenience to use a
:class:`requests.Session` and ``requests.auth`` compatible authentication
option (Auth tuple or callable to enable Basic/Digest/Custom HTTP Auth),
which is useful when third party libraries offer such helpers (ex:
`requests-aws <https://pypi.org/project/requests-aws/>`_).

Example using :class:`sgqlc.endpoint.requests.RequestsEndpoint`:

.. literalinclude:: ../../examples/basic/03_requests_endpoint.py
   :language: python

The ``query`` may be given as ``bytes`` or ``str`` as in the example, but
it may be a :class:`sgqlc.operation.Operation`, which will serialize as
string while also providing convenience to interepret the results.

See `more examples <https://github.com/profusion/sgqlc/tree/master/examples>`_.

:license: ISC
'''

__docformat__ = 'reStructuredText en'

__all__ = ('RequestsEndpoint',)

import json
import logging
import requests


from .base import BaseEndpoint, add_query_to_url


class RequestsEndpoint(BaseEndpoint):
    '''GraphQL access over HTTP.

    This helper is very thin, just setups the correct HTTP request to
    GraphQL endpoint, handling logging of HTTP and GraphQL errors. The
    object is callable with parameters: ``query``, ``variables``,
    ``operation_name``, ``extra_headers`` and ``timeout``.

    The user of this class should create GraphQL queries and interpret the
    resulting object, created from JSON data, with top level properties:

    :data: object matching the GraphQL requests, or ``null`` if only
       errors were returned.

    :errors: list of errors, which are objects with the key "message" and
       optionally others, such as "location" (for errors matching GraphQL
       input). Instead of raising exceptions, such as
       :exc:`requests.exceptions.HTTPError` or
       :exc:`json.JSONDecodeError` those are stored in the
       "exception" key.

    .. note::

      Both ``data`` and ``errors`` may be returned, for instance if
      a null-able field fails, it will be returned as null (Python
      ``None``) in data the associated error in the array.

    The class has its own :class:`logging.Logger` which is used to
    debug, info, warning and errors. Error logging and conversion to
    uniform data structure similar to GraphQL, with ``{"errors": [...]}``
    is done by :func:`RequestsEndpoint._log_http_error()` own method,
    ``BaseEndpoint._log_json_error()`` and
    ``BaseEndpoint._log_graphql_error()``. This last one will show the
    snippets of GraphQL that failed execution.
    '''

    logger = logging.getLogger(__name__)

    def __init__(self, url, base_headers=None, timeout=None, method='POST',
                 auth=None, session=None):
        '''
        :param url: the default GraphQL endpoint url.
        :type url: str

        :param base_headers: the base HTTP headers to include in every request.
        :type base_headers: dict

        :param timeout: timeout in seconds to use with
          :func:`urllib.request.urlopen`. Optional (``None`` uses
          default timeout).
        :type timeout: float

        :param method: HTTP Method to use for the request,
                       `POST` is used by default

        :param auth: ``requests.auth`` compatible authentication option.
          Auth tuple or callable to enable Basic/Digest/Custom HTTP Auth.
          Optional.

        :param session: :class:`requests.Session` object. Optional.
        '''
        self.url = url
        self.base_headers = base_headers or {}
        self.timeout = timeout
        self.method = method
        self.auth = auth
        self.session = session

    def __str__(self):
        return ('%s(url=%s, base_headers=%r, timeout=%r, '
                'method=%s, auth=%s, session=%s)') % (
            self.__class__.__name__, self.url, self.base_headers, self.timeout,
            self.method,
            self.auth.__class__ if self.auth is not None else None,
            self.session.__class__ if self.session is not None else None)

    def __call__(self, query, variables=None,  # noqa: C901
                 operation_name=None, extra_headers=None, timeout=None):
        '''Calls the GraphQL endpoint.

        :param query: the GraphQL query or mutation to execute. Note
          that this is converted using ``bytes()``, thus one may pass
          an object implementing ``__bytes__()`` method to return the
          query, eventually in more compact form (no indentation, etc).
        :type query: :class:`str` or :class:`bytes`.

        :param variables: variables (dict) to use with
          ``query``. This is only useful if the query or
          mutation contains ``$variableName``.
          Must be a **plain JSON-serializeable object**
          (dict with string keys and values being one of dict, list, tuple,
          str, int, float, bool, None... -- :func:`json.dumps` is used)
          and the keys must **match exactly** the variable names (no name
          conversion is done, no dollar-sign prefix ``$`` should be used).
        :type variables: dict

        :param operation_name: if more than one operation is listed in
          ``query``, then it should specify the one to be executed.
        :type operation_name: str

        :param extra_headers: dict with extra HTTP headers to use.
        :type extra_headers: dict

        :param timeout: overrides the default timeout.
        :type timeout: float

        :return: dict with optional fields ``data`` containing the GraphQL
          returned data as nested dict and ``errors`` with an array of
          errors. Note that both ``data`` and ``errors`` may be returned!
        :rtype: dict
        '''
        if isinstance(query, bytes):
            query = query.decode('utf-8')
        elif not isinstance(query, str):
            # allows sgqlc.operation.Operation to be passed
            # and generate compact representation of the queries
            query = bytes(query).decode('utf-8')

        headers = self.base_headers.copy()
        if extra_headers:
            headers.update(extra_headers)

        if 'Accept' not in headers:
            headers['Accept'] = 'application/json; charset=utf-8'

        if self.method.upper() == 'POST':
            get_http_request = self.get_http_post_request
        else:
            get_http_request = self.get_http_get_request

        req = get_http_request(query, variables, operation_name, headers)

        self.logger.debug('Query:\n%s', query)

        try:
            with self.session if self.session is not None \
                    else requests.Session() as session:
                prepped = session.prepare_request(req)
                with session.send(prepped,
                                  timeout=timeout or self.timeout) as f:
                    try:
                        f.raise_for_status()
                        data = f.json()
                        if data and data.get('errors'):
                            return self._log_graphql_error(query, data)
                        return data
                    except json.JSONDecodeError as exc:
                        return self._log_json_error(f.text, exc)
        except requests.exceptions.HTTPError as exc:
            return self._log_http_error(query, req, exc)

    def get_http_post_request(self, query, variables, operation_name, headers):
        post_data = json.dumps({
            'query': query,
            'variables': variables,
            'operationName': operation_name,
        }).encode('utf-8')
        headers.update({
            'Content-Type': 'application/json; charset=utf-8'
        })
        return requests.Request(
            url=self.url, auth=self.auth, data=post_data,
            headers=headers,
            method='POST')

    def get_http_get_request(self, query, variables, operation_name, headers):
        params = {'query': query}
        if operation_name:
            params['operationName'] = operation_name

        if variables:
            params['variables'] = json.dumps(variables)

        url = add_query_to_url(self.url, params)
        return requests.Request(url=url, auth=self.auth, headers=headers,
                                method='GET')

    def _log_http_error(self, query, req, exc):
        '''Log :exc:`requests.exceptions.HTTPError`, converting to
        GraphQL's ``{"data": null, "errors": [{"message": str(exc)...}]}``

        :param query: the GraphQL query that triggered the result.
        :type query: str

        :param req: :class:`requests.Request` instance that was opened.
        :type req: :class:`requests.Request`

        :param exc: :exc:`requests.exceptions.HTTPError` instance
        :type exc: :exc:`requests.exceptions.HTTPError`

        :return: GraphQL-compliant dict with keys ``data`` and ``errors``.
        :rtype: dict
        '''
        self.logger.error('log_error - %s: %s', req.url, exc)
        for h in sorted(exc.response.headers):
            self.logger.info('Response header: %s: %s', h,
                             exc.response.headers[h])

        body = exc.response.text
        content_type = exc.response.headers.get('Content-Type', '')
        self.logger.info('Response [%s]:\n%s', content_type, body)
        if not content_type.startswith('application/json'):
            return {'data': None, 'errors': [{
                'message': str(exc),
                'exception': exc,
                'status': exc.response.status_code,
                'headers': exc.response.headers,
                'body': body,
            }]}
        else:
            # GraphQL servers return 400 and {'errors': [...]}
            # if only errors was returned, no {'data': ...}
            try:
                data = json.loads(body)
            except json.JSONDecodeError as exc:
                return self._log_json_error(body, exc)

            if isinstance(data, dict) and data.get('errors'):
                data.update({
                    'exception': exc,
                    'status': exc.response.status_code,
                    'headers': exc.response.headers,
                })
                return self._log_graphql_error(query, data)
            return {'data': None, 'errors': [{
                'message': str(exc),
                'exception': exc,
                'status': exc.response.status_code,
                'headers': exc.response.headers,
                'body': body,
            }]}


if __name__ == '__main__':  # pragma: no cover
    import argparse
    import sys

    def tuple_arg(s):
        p = s.split('=', 1)
        if len(p) == 2:
            return p
        return s.split(':', 1)

    ap = argparse.ArgumentParser(
        description='Access GraphQL endpoint using HTTP',
    )

    # Generic options to access the GraphQL API
    ap.add_argument('url', help='GraphQL endpoint address.')
    ap.add_argument('query', help='GraphQL query or mutation.')

    ap.add_argument('--var', '-V', action='append', type=tuple_arg,
                    help='NAME=VALUE variable to send alongside query.',
                    default=[])
    ap.add_argument('--operation', '-o',
                    help='GraphQL operation name to send alongside query.',
                    default=None)
    ap.add_argument('--header', '-H', action='append', type=tuple_arg,
                    help=('NAME=VALUE HTTP header to send. '
                          'Example: "Authorization: bearer ${token}"'),
                    default=[])
    ap.add_argument('--timeout', '-t', type=float, default=None,
                    help='Request timeout, in seconds.')
    ap.add_argument('--verbose', '-v',
                    help='Increase verbosity',
                    action='count',
                    default=0)
    ap.add_argument('--method', '-m',
                    choices=['GET', 'POST'],
                    help='HTTP Method to use',
                    default='POST',
                    )

    args = ap.parse_args()

    logfmt = '%(levelname)s: %(message)s'
    logging.basicConfig(format=logfmt, level=max(10, 40 - (args.verbose * 10)))

    endpoint = RequestsEndpoint(args.url, dict(args.header), args.timeout,
                                method=args.method)
    data = endpoint(args.query, dict(args.var))

    json.dump(data, sys.stdout, sort_keys=True, indent=2, default=str)
    sys.stdout.write('\n')
    if data.get('errors'):
        sys.exit(1)
