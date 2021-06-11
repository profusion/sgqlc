from sgqlc.endpoint.base import BaseEndpoint
import websocket
import uuid
import json


class WebSocketEndpoint(BaseEndpoint):
    '''
    A synchronous websocket endpoint for graphql queries or subscriptions
    '''
    def __init__(self, url, connection_payload=None, **ws_options):
        '''
        :param url: ws:// or wss:// url to connect to
        :type url: str

        :param connection_payload: data to pass during initiation of the
          WebSocket connection. It's passed as ``"payload"`` key of the
          ``connection_init`` type message. **Authentication tokens** usually
          goes here.
        :type connection_payload: dict

        :param ws_options: options to pass to
          :func:`websocket._core.create_connection`.
        :type ws_options: dict
        '''
        self.url = url
        self.connection_payload = connection_payload
        self.ws_options = ws_options
        self.keep_alives = ['ka']

    def __str__(self):
        return '%s(url=%s, ws_options=%s)' % (
            self.__class__.__name__, self.url, self.ws_options)

    def __call__(self, query, variables=None, operation_name=None):
        '''
        Makes a single query over the websocket

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

        :return: generator of dicts with optional fields ``data`` containing
          the GraphQL returned data as nested dict and ``errors`` with
          an array of errors. Note that both ``data`` and ``errors`` may
          be returned in each dict!
          Will generate a single element for ``query`` operations,
          where data lists are generally embedded within the result structure.
          For ``subscription`` operations, will generate a dict for each
          subscription notification.

        :rtype: generator
        '''
        if isinstance(query, bytes):
            query = query.decode('utf-8')
        elif not isinstance(query, str):
            # allows sgqlc.operation.Operation to be passed
            # and generate compact representation of the queries
            query = bytes(query).decode('utf-8')
        ws = websocket.create_connection(self.url,
                                         subprotocols=['graphql-ws'],
                                         **self.ws_options)
        try:
            init_id = self.generate_id()
            connection_setup_dict = {'type': 'connection_init', 'id': init_id}
            if self.connection_payload:
                connection_setup_dict['payload'] = self.connection_payload
            ws.send(json.dumps(connection_setup_dict))

            response = self._get_response(ws)
            if response['type'] != 'connection_ack':
                raise ValueError(
                    f'Unexpected {response["type"]} '
                    f'when waiting for connection ack'
                )
            # response does not always have an id
            if response.get('id', init_id) != init_id:
                raise ValueError(
                    f'Unexpected id {response["id"]} '
                    f'when waiting for connection ack'
                )

            query_id = self.generate_id()
            ws.send(json.dumps({'type': 'start',
                                'id': query_id,
                                'payload': {'query': query,
                                            'variables': variables,
                                            'operationName': operation_name}}))
            response = self._get_response(ws)
            while response['type'] != 'complete':
                if response['id'] != query_id:
                    raise ValueError(
                        f'Unexpected id {response["id"]} '
                        f'when waiting for query results'
                    )
                if response['type'] == 'data':
                    yield response['payload']
                else:
                    raise ValueError(f'Unexpected message {response} '
                                     f'when waiting for query results')
                response = self._get_response(ws)

        finally:
            ws.close()

    def _get_response(self, ws):
        '''Ignore any keep alive responses'''

        response = json.loads(ws.recv())
        while response['type'] in self.keep_alives:
            response = json.loads(ws.recv())
        return response

    @staticmethod
    def generate_id() -> str:
        return str(uuid.uuid4())
