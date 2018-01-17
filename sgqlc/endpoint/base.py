'''
sgqlc - Simple GraphQL Client
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Base Endpoint
=============

Base interface for endpoints.

:license: ISC
'''

__docformat__ = 'reStructuredText en'

__all__ = ('BaseEndpoint',)

import logging


class BaseEndpoint:
    '''GraphQL endpoint access.

    The user of this class should create GraphQL queries and interpret the
    resulting object, created from JSON data, with top level properties:

    :data: object matching the GraphQL requests, or ``null`` if only
       errors were returned.

    :errors: list of errors, which are objects with the key "message" and
       optionally others, such as "location" (for errors matching GraphQL
       input). Instead of raising exceptions, such as
       :exc:`json.JSONDecodeError` those are stored in the
       "exception" key. Subclasses should extend errors providing
       meaningful messages and extra payload.

    .. note::

      Both ``data`` and ``errors`` may be returned, for instance if
      a null-able field fails, it will be returned as null (Python
      ``None``) in data the associated error in the array.

    The class has its own :class:`logging.Logger` which is used to
    debug, info, warning and errors. Note that subclasses may override
    this logger. Error logging and conversion to uniform data
    structure similar to GraphQL, with ``{"errors": [...]}``
    is done by :func:`BaseEndpoint._log_json_error()` and
    :func:`BaseEndpoint._log_graphql_error()` methods. This last one
    will show the snippets of GraphQL that failed execution.
    '''

    logger = logging.getLogger(__name__)

    def __call__(self, query, variables=None, operation_name=None):
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

        :return: dict with optional fields ``data`` containing the GraphQL
          returned data as nested dict and ``errors`` with an array of
          errors. Note that both ``data`` and ``errors`` may be returned!
        :rtype: dict

        .. note::

          Subclasses **must** implement this method, should respect
          this base signature and may extend with extra parameters
          such as timeout, extra headers and so on.
        '''
        raise NotImplementedError()

    def _log_json_error(self, body, exc):
        '''Log a :exc:`json.JSONDecodeError`, converting to
        GraphQL's ``{"data": null, "errors": [{"message": str(exc)...}]}``

        :param body: the string with JSON document.
        :type body: str

        :param exc: the :exc:`json.JSONDecodeError`
        :type exc: :exc:`json.JSONDecodeError`

        :return: GraphQL-compliant dict with keys ``data`` and ``errors``.
        :rtype: dict
        '''
        self.logger.error('could not decode JSON response: %s', exc)
        return {'data': None, 'errors': [{
            'message': str(exc),
            'exception': exc,
            'body': body,
        }]}

    def _log_graphql_error(self, query, data):
        '''Log a ``{"errors": [...]}`` GraphQL return and return itself.

        :param query: the GraphQL query that triggered the result.
        :type query: str

        :param data: the decoded JSON object.
        :type data: dict

        :return: the input ``data``
        :rtype: dict
        '''
        if isinstance(query, bytes):
            query = query.decode('utf-8')
        elif not isinstance(query, str):
            # allows sgqlc.operation.Operation to be passed
            # and generate compact representation of the queries
            query = bytes(query).decode('utf-8')

        errors = data['errors']
        self.logger.error('GraphQL query failed with %s errors', len(errors))
        for i, error in enumerate(errors):
            paths = error.get('path')
            if paths:
                paths = ' ' + '/'.join(paths)
            else:
                paths = ''
            self.logger.info('Error #{}{}:'.format(i, paths))
            for ln in error.get('message', '').split('\n'):
                self.logger.info('   | {}'.format(ln))

            s = self.snippet(query, error.get('locations'))
            if s:
                self.logger.info('   -')
                self.logger.info('   | Locations:')
                for ln in s:
                    self.logger.info('   | {}'.format(ln))
        return data

    @staticmethod
    def snippet(code, locations, sep=' | ', colmark=('-', '^'), context=5):
        '''Given a code and list of locations, convert to snippet lines.

        return will include line number, a separator (``sep``), then
        line contents.

        At most ``context`` lines are shown before each location line.

        After each location line, the column is marked using
        ``colmark``. The first character is repeated up to column, the
        second character is used only once.

        :return: list of lines of sources or column markups.
        :rtype: list
        '''
        if not locations:
            return []
        lines = code.split('\n')
        offset = int(len(lines) / 10) + 1
        linenofmt = '%{}d'.format(offset)
        s = []
        for loc in locations:
            line = max(0, loc.get('line', 1) - 1)
            column = max(0, loc.get('column', 1) - 1)
            start_line = max(0, line - context)
            for i, ln in enumerate(lines[start_line:line + 1], start_line):
                s.append('{}{}{}'.format(linenofmt % i, sep, ln))
            s.append('{}{}{}'.format(' ' * (offset + len(sep)),
                                     colmark[0] * column,
                                     colmark[1]))
        return s
