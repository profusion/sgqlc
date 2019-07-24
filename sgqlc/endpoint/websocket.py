from typing import Dict, Any, Union, SupportsBytes, Iterable
from websocket import WebSocket

from sgqlc.endpoint.base import BaseEndpoint
import websocket
import uuid
import json


class CancelableResultGenerator:
    '''
    Generator of websocket subscription notification events that supports
    sending a message to the server to cancel the subscription.
    '''
    def __init__(self, ws: WebSocket, query_id: str, should_close: bool):
        '''
        :param ws: websocket to get results from
        :type ws: WebSocket

        :param query_id: query_id to track
        :type query_id: str

        :param should_close: whether to close the socket after
          completing iteration on the results
        :type should_close: bool
        '''
        self.ws = ws
        self.query_id = query_id
        self.should_close = should_close

    def __next__(self) -> dict:
        response = json.loads(self.ws.recv())
        if response['id'] != self.query_id:
            raise ValueError(
                f'Unexpected id {response["id"]} '
                f'when waiting for query results'
            )
        if response['type'] == 'data':
            return response['payload']
        elif response['type'] == 'complete':
            if self.should_close:
                self.ws.close()
            raise StopIteration()
        else:
            raise ValueError(f'Unexpected message {response} '
                             f'when waiting for query results')

    def __iter__(self):
        return self

    def cancel(self):
        self.ws.send(json.dumps({'type': 'stop', 'id': self.query_id}))


class WebSocketEndpoint(BaseEndpoint):
    '''
    A websocket endpoint for graphql queries or subscriptions.
    Will return a generator of response objects when called.
    '''
    def __init__(self, url: str = None, ws: WebSocket = None, **ws_options):
        '''
        :param url: ws:// or wss:// url to connect to
        :type url: str

        :param ws: existing websocket connection to use instead of
          creating a new one.  if passing an existing connection,
          the calling code is responsible for both closing it and
          handling the ``connection_init``/``connection ack``
          handshake.
        :type ws: WebSocket

        :param ws_options: options to pass to websocket.create_connection
        :type ws_options: dict
        '''
        self.url = url
        self.ws = ws
        self.ws_options = ws_options

    def __str__(self) -> str:
        return '%s(url=%s, ws_options=%s)' % (
            self.__class__.__name__, self.url, self.ws_options)

    def _create_connection(self) -> WebSocket:
        '''
        Create a new websocket connection and handle the
        ``connection_init``/``connection_ack`` handshake.
        :return: websocket connection
        :rtype: WebSocket
        '''
        ws = websocket.create_connection(self.url,
                                         subprotocols=['graphql-ws'],
                                         **self.ws_options)
        init_id = self.generate_id()
        ws.send(json.dumps({'type': 'connection_init', 'id': init_id}))
        response = json.loads(ws.recv())
        if response['type'] != 'connection_ack':
            raise ValueError(
                f'Unexpected {response["type"]} '
                f'when waiting for connection ack'
            )
        if response['id'] != init_id:
            raise ValueError(
                f'Unexpected id {response["id"]} '
                f'when waiting for connection ack'
            )
        return ws

    def __call__(self,
                 query: Union[str, Union[bytes, SupportsBytes]],
                 variables: Dict[str, Any] = None,
                 operation_name: str = None) -> Iterable:
        '''
        Makes a single query over the websocket

        :param query: the GraphQL query, subscription, or mutation to
          execute. Note that this is converted using ``bytes()``, thus
          one may pass an object implementing ``__bytes__()`` method to
          return the query, eventually in more compact form (no
          indentation, etc).
        :type query: :class:`str` or :class:`bytes`.

        :param variables: variables (dict) to use with
          ``query``. This is only useful if the query or
          mutation contains ``$variableName``.
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
        ws = self.ws
        if not ws:
            ws = self._create_connection()

        query_id = self.generate_id()
        ws.send(json.dumps({'type': 'start',
                            'id': query_id,
                            'payload': {'query': query,
                                        'variables': variables,
                                        'operationName': operation_name}}))
        return CancelableResultGenerator(ws, query_id, not self.ws)

    @staticmethod
    def generate_id() -> str:
        return str(uuid.uuid4())
