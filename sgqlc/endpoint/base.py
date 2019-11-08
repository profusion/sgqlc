'''
Base Endpoint
=============

Base interface for endpoints.

:license: ISC
'''

__docformat__ = 'reStructuredText en'

__all__ = ('BaseEndpoint',)

import logging
import urllib.parse


def add_query_to_url(url, extra_query):
    '''Adds an extra query to URL, returning the new URL.

    Extra query may be a dict or a list as returned by
    :func:`urllib.parse.parse_qsl()` and :func:`urllib.parse.parse_qs()`.

    '''
    split = urllib.parse.urlsplit(url)
    merged_query = urllib.parse.parse_qsl(split.query)
    if isinstance(extra_query, dict):
        for k, v in extra_query.items():
            if not isinstance(v, (tuple, list)):
                merged_query.append((k, v))
            else:
                for cv in v:
                    merged_query.append((k, cv))
    else:
        merged_query.extend(extra_query)

    merged_split = urllib.parse.SplitResult(
        split.scheme,
        split.netloc,
        split.path,
        urllib.parse.urlencode(merged_query),
        split.fragment,
    )
    return merged_split.geturl()


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
        raise NotImplementedError()  # pragma: no cover

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

    def _fixup_graphql_error(self, data):
        '''Given a possible GraphQL error payload, make sure it's in shape.

        This will ensure the given ``data`` is in the shape:

        .. code-block:: json

           {"errors": [{"message": "some string"}]}

        If ``errors`` is not an array, it will be made into a single element
        array, with the object in that format, with its string representation
        being the message.

        If an element of the ``errors`` array is not in the format, then
        it's converted to the format, with its string representation being
        the message.

        The input object is not changed, a copy is made if needed.

        :return: the given ``data`` formatted to the correct shape, a copy
                 is made and returned if any fix up was needed.
        :rtype: dict
        '''
        original_data = data
        errors = data.get('errors')
        original_errors = errors
        if not isinstance(errors, list):
            self.logger.warning('data["errors"] is not a list! Fix up data=%r',
                                data)
            data = data.copy()
            data['errors'] = [{'message': str(errors)}]
            return data

        for i, error in enumerate(errors):
            if not isinstance(error, dict):
                self.logger.warning('Error #%d: is not a dict: %r. Fix up!',
                                    i, error)
                if data is original_data:
                    data = data.copy()
                if errors is original_errors:
                    errors = errors.copy()
                    data['errors'] = errors

                errors[i] = {'message': str(error)}
                continue

            message = error.get('message')
            if not isinstance(message, str):
                if data is original_data:
                    data = data.copy()
                if errors is original_errors:
                    errors = errors.copy()
                    data['errors'] = errors

                message = str(error) if message is None else str(message)
                error = error.copy()
                error['message'] = message
                errors[i] = error

        return data

    def _log_graphql_error(self, query, data):
        '''Log a ``{"errors": [...]}`` GraphQL return and return itself.

        :param query: the GraphQL query that triggered the result.
        :type query: str

        :param data: the decoded JSON object.
        :type data: dict

        :return: the input ``data``
        :rtype: dict
        '''
        if isinstance(query, bytes):  # pragma: no cover
            query = query.decode('utf-8')
        elif not isinstance(query, str):  # pragma: no cover
            # allows sgqlc.operation.Operation to be passed
            # and generate compact representation of the queries
            query = bytes(query).decode('utf-8')

        data = self._fixup_graphql_error(data)
        errors = data['errors']
        self.logger.error('GraphQL query failed with %s errors', len(errors))
        for i, error in enumerate(errors):
            paths = error.get('path')
            if paths:
                paths = ' ' + '/'.join(str(path) for path in paths)
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
