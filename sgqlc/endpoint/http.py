'''
sgqlc - Simple GraphQL Client
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Synchronous HTTP Endpoint
=========================

This endpoint implements GraphQL client using
:func:`urllib.request.urlopen()` or compatible function.

This module provides command line utility:

.. code-block:: console

   $ python3 -m sgqlc.endpoint.http http://server.com/ '{ queryHere { ... } }'

:license: ISC
'''

__docformat__ = 'reStructuredText en'

__all__ = ('HTTPEndpoint',)

import json
import logging
import urllib.error
import urllib.request
import urllib.parse

from .base import BaseEndpoint


class HTTPEndpoint(BaseEndpoint):
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
       :exc:`urllib.error.HTTPError` or
       :exc:`json.JSONDecodeError` those are stored in the
       "exception" key.

    .. note::

      Both ``data`` and ``errors`` may be returned, for instance if
      a null-able field fails, it will be returned as null (Python
      ``None``) in data the associated error in the array.

    The class has its own :class:`logging.Logger` which is used to
    debug, info, warning and errors. Error logging and conversion to
    uniform data structure similar to GraphQL, with ``{"errors": [...]}``
    is done by :func:`HTTPEndpoint._log_http_error()` own method,
    ``BaseEndpoint._log_json_error()`` and
    ``BaseEndpoint._log_graphql_error()``. This last one will show the
    snippets of GraphQL that failed execution.
    '''

    logger = logging.getLogger(__name__)

    def __init__(self, url, base_headers=None, timeout=None, urlopen=None):
        '''
        :param url: the default GraphQL endpoint url.
        :type url: str

        :param base_headers: the base HTTP headers to include in every request.
        :type base_headers: dict

        :param timeout: timeout in seconds to use with
          :func:`urllib.request.urlopen`. Optional (``None`` uses
          default timeout).
        :type timeout: float

        :param urlopen: function that implements the same interface as
          :func:`urllib.request.urlopen`, which is used by default.
        '''
        self.url = url
        self.base_headers = base_headers or {}
        self.timeout = timeout
        self.urlopen = urlopen or urllib.request.urlopen

    def __str__(self):
        return '%s(url=%s, base_headers=%r, timeout=%r)' % (
            self.__class__.__name__, self.url, self.base_headers, self.timeout)

    def __call__(self, query, variables=None, operation_name=None,
                 extra_headers=None, timeout=None):
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

        post_data = json.dumps({
            'query': query,
            'variables': variables,
            'operationName': operation_name,
        }).encode('utf-8')
        headers = self.base_headers.copy()
        if extra_headers:
            headers.update(extra_headers)
        headers.update({
            'Accept': 'application/json; charset=utf-8',
            'Content-Type': 'application/json; charset=utf-8',
            'Content-Length': len(post_data),
        })

        self.logger.debug('Query:\n%s', query)

        target = f'{self.url}?query={urllib.parse.quote_plus(query)}'
        req = urllib.request.Request(
            url=target, data=post_data, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=timeout) as f:
                body = f.read().decode('utf-8')
                try:
                    data = json.loads(body)
                    if data and data.get('errors'):
                        return self._log_graphql_error(query, data)
                    return data
                except json.JSONDecodeError as exc:
                    return self._log_json_error(body, exc)
        except urllib.error.HTTPError as exc:
            return self._log_http_error(query, req, exc)

    def _log_http_error(self, query, req, exc):
        '''Log :exc:`urllib.error.HTTPError`, converting to
        GraphQL's ``{"data": null, "errors": [{"message": str(exc)...}]}``

        :param query: the GraphQL query that triggered the result.
        :type query: str

        :param req: :class:`urllib.request.Request` instance that was opened.
        :type req: :class:`urllib.request.Request`

        :param exc: :exc:`urllib.error.HTTPError` instance
        :type exc: :exc:`urllib.error.HTTPError`

        :return: GraphQL-compliant dict with keys ``data`` and ``errors``.
        :rtype: dict
        '''
        self.logger.error('%s: %s', req.get_full_url(), exc)
        for h in sorted(exc.headers):
            self.logger.info('Response header: %s: %s', h, exc.headers[h])

        body = exc.read().decode('utf-8')
        content_type = exc.headers.get('Content-Type', '')
        self.logger.info('Response [%s]:\n%s', content_type, body)
        if not content_type.startswith('application/json'):
            return {'data': None, 'errors': [{
                'message': str(exc),
                'exception': exc,
                'status': exc.code,
                'headers': exc.headers,
                'body': body,
            }]}
        else:
            # GraphQL servers return 400 and {'errors': [...]}
            # if only errors was returned, no {'data': ...}
            data = json.loads(body)
            if data and data.get('errors'):
                return self._log_graphql_error(query, data)
            return {'data': None, 'errors': [{
                'message': str(exc),
                'exception': exc,
                'status': exc.code,
                'headers': exc.headers,
                'body': body,
            }]}


if __name__ == '__main__':
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

    args = ap.parse_args()

    logfmt = '%(levelname)s: %(message)s'
    logging.basicConfig(format=logfmt, level=max(10, 40 - (args.verbose * 10)))

    endpoint = HTTPEndpoint(args.url, dict(args.header), args.timeout)
    data = endpoint(args.query, dict(args.var))

    json.dump(data, sys.stdout, sort_keys=True, indent=2, default=str)
    sys.stdout.write('\n')
    if data.get('errors'):
        sys.exit(1)
