from typing import Any, Dict, Union, SupportsBytes
from websocket import WebSocket

from sgqlc.endpoint.base import BaseEndpoint
import websocket
import uuid
import json


def _receive_message(ws: WebSocket) -> Dict[Any, Any]:
    '''
    Receive and return  message from the websocket,
    discarding any keepalive messages

    :param ws: websocket to listen on
    :type ws: WebSocket

    :return: message from the server
    :rtype: dict
    '''
    response = {'type': 'ka'}
    while response['type'] == 'ka':
        response = json.loads(ws.recv())
    return response


class CancelableResultGenerator:
    '''
    Generator of websocket subscription notification events that supports
    sending a message to the server to cancel the subscription.
    '''
    def __init__(self, ws: WebSocket, query_id: str):
        '''
        :param ws: websocket to get results from
        :type ws: WebSocket

        :param query_id: query_id to track
        :type query_id: str
        '''
        self.ws = ws
        self.query_id = query_id

    def __next__(self) -> dict:
        response = _receive_message(self.ws)
        if response['id'] != self.query_id:
            raise ValueError(
                f'Unexpected id {response["id"]} '
                f'when waiting for query results'
            )
        if response['type'] == 'data':
            return response['payload']
        elif response['type'] == 'complete':
            self.ws.close()
            raise StopIteration()
        else:
            raise ValueError(f'Unexpected message {response} '
                             f'when waiting for query results')

    def __iter__(self):
        return self

    def cancel(self):
        self.ws.send(json.dumps({'type': 'stop',
                                 'id': self.query_id,
                                 'payload': None}))


class WebSocketEndpoint(BaseEndpoint):
    '''
    A synchronous websocket endpoint for graphql queries or subscriptions
    '''
    def __init__(self, url: str, **ws_options: Dict[Any, Any]):
        '''
        :param url: ws:// or wss:// url to connect to
        :type url: str

        :param ws_options: options to pass to websocket.create_connection
        :type ws_options: dict
        '''
        self.url = url
        self.ws_options = ws_options

    def __str__(self) -> str:
        return '%s(url=%s, ws_options=%s)' % (
            self.__class__.__name__, self.url, self.ws_options)

    def __call__(self,
                 query: Union[str, Union[bytes, SupportsBytes]],
                 variables: Dict[str, Any] = None,
                 operation_name: str = None) -> CancelableResultGenerator:
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
        ws = websocket.create_connection(self.url,
                                         subprotocols=['graphql-ws'],
                                         **self.ws_options)
        try:
            init_id = self.generate_id()
            ws.send(json.dumps({'type': 'connection_init',
                                'id': init_id,
                                'payload': None}))
            response = _receive_message(ws)
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

            query_id = self.generate_id()
            ws.send(json.dumps({'type': 'start',
                                'id': query_id,
                                'payload': {'query': query,
                                            'variables': variables,
                                            'operationName': operation_name}}))
            return CancelableResultGenerator(ws, query_id)
        except Exception as e:
            ws.close()
            raise e

    @staticmethod
    def generate_id() -> str:
        return str(uuid.uuid4())
