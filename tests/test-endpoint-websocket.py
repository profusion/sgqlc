import json
import re
from unittest.mock import patch, Mock

from sgqlc.endpoint.websocket import WebSocketEndpoint
from nose.tools import eq_

from sgqlc.operation import Operation
from sgqlc.types import Schema, Type

test_url = 'ws://localhost:12345/graphql'
endpoint = WebSocketEndpoint(test_url)
endpoint.generate_id = lambda: '123'


def test_endpoint_str():
    'Test websocket str() implementation'
    eq_(
        str(endpoint),
        'WebSocketEndpoint(' + 'url={}'.format(test_url) + ', ws_options={})',
    )


def test_endpoint_id():
    'Test websocket uuid generation'
    generated_id = WebSocketEndpoint('').generate_id()
    eq_(
        re.match(
            '[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}',
            generated_id,
        )
        is not None,
        True,
    )


@patch('sgqlc.endpoint.websocket.websocket')
def test_basic_query(mock_websocket):
    'Test websocket endpoint against simple query'
    mock_connection = Mock()
    mock_websocket.create_connection.return_value = mock_connection
    mock_connection.recv.side_effect = [
        """
        {
            "type": "connection_ack",
            "id": "123"
        }
        """,
        """
        {
            "type": "data",
            "id": "123",
            "payload": {
                "data": {"test": ["1", "2"]}
            }
        }
        """,
        """
        {
            "type": "complete",
            "id": "123"
        }
        """,
    ]
    eq_(list(endpoint('query {test}')), [{'data': {'test': ['1', '2']}}])


@patch('sgqlc.endpoint.websocket.websocket')
def test_basic_query_apollo(mock_websocket):
    '''Test websocket endpoint against simple apollo query with keepalive
    and no id in connection_ack'''
    mock_connection = Mock()
    mock_websocket.create_connection.return_value = mock_connection
    mock_connection.recv.side_effect = [
        """
        {
            "type": "connection_ack"
        }
        """,
        """
        {
            "type": "ka"
        }
        """,
        """
        {
            "type": "ka"
        }
        """,
        """
        {
            "type": "data",
            "id": "123",
            "payload": {
                "data": {"test": ["1", "2"]}
            }
        }
        """,
        """
        {
            "type": "ka"
        }
        """,
        """
        {
            "type": "ka"
        }
        """,
        """
        {
            "type": "complete",
            "id": "123"
        }
        """,
    ]
    eq_(list(endpoint('query {test}')), [{'data': {'test': ['1', '2']}}])


@patch('sgqlc.endpoint.websocket.websocket')
def test_operation_query(mock_websocket):
    'Test if query with type sgqlc.operation.Operation() or raw bytes works'

    schema = Schema()

    # MyType and Query may be declared if doctests were processed by nose
    if 'MyType' in schema:
        schema -= schema.MyType

    if 'Query' in schema:
        schema -= schema.Query

    class MyType(Type):
        __schema__ = schema
        i = int

    class Query(Type):
        __schema__ = schema
        my_type = MyType

    op = Operation(Query)
    op.my_type.i()

    mock_connection = Mock()
    mock_websocket.create_connection.return_value = mock_connection
    return_values = [
        """
        {
            "type": "connection_ack",
            "id": "123"
        }
        """,
        """
        {
            "type": "data",
            "id": "123",
            "payload": {
                "data": {"test": ["1", "2"]}
            }
        }
        """,
        """
        {
            "type": "complete",
            "id": "123"
        }
        """,
    ]
    # query twice so double ret values twice
    return_values.extend(return_values)
    mock_connection.recv.side_effect = return_values
    eq_(list(endpoint(op)), [{'data': {'test': ['1', '2']}}])
    eq_(list(endpoint(bytes(op))), [{'data': {'test': ['1', '2']}}])
    eq_(
        bytes(
            json.loads(mock_connection.send.call_args_list[1][0][0])[
                'payload'
            ]['query'],
            encoding='utf-8',
        ),
        bytes(op),
    )


@patch('sgqlc.endpoint.websocket.websocket')
def test_basic_subscription(mock_websocket):
    'Test websocket endpoint against simple subscription query'
    mock_connection = Mock()
    mock_websocket.create_connection.return_value = mock_connection
    mock_connection.recv.side_effect = [
        """
        {
            "type": "connection_ack",
            "id": "123"
        }
        """,
        """
        {
            "type": "data",
            "id": "123",
            "payload": {
                "data": {"test": "1"}
            }
        }
        """,
        """
        {
            "type": "data",
            "id": "123",
            "payload": {
                "data": {"test": "2"}
            }
        }
        """,
        """
        {
            "type": "complete",
            "id": "123"
        }
        """,
    ]
    eq_(
        list(endpoint('subscription {test}')),
        [{'data': {'test': '1'}}, {'data': {'test': '2'}}],
    )


@patch('sgqlc.endpoint.websocket.websocket')
def test_authenticated_subscription(mock_websocket):
    'Test websocket endpoint against subscription with authentication token'
    mock_connection = Mock()
    mock_websocket.create_connection.return_value = mock_connection
    mock_connection.recv.side_effect = [
        """
        {
            "type": "connection_ack",
            "id": "123"
        }
        """,
        """
        {
            "type": "complete",
            "id": "123"
        }
        """,
    ]
    connection_payload = {'authToken': 'MyAuthTokenForSubscription'}

    authenticated_endpoint = WebSocketEndpoint(
        test_url,
        connection_payload=connection_payload,
    )
    authenticated_endpoint.generate_id = endpoint.generate_id
    list(authenticated_endpoint('subscription {test}'))

    authenticate_call_args = json.loads(
        mock_connection.send.call_args_list[0][0][0]
    )
    eq_(
        authenticate_call_args,
        {
            'type': 'connection_init',
            'id': '123',
            'payload': connection_payload,
        },
    )


@patch('sgqlc.endpoint.websocket.websocket')
def test_unexpected_ack(mock_websocket):
    'Test bad message type when waiting for ack'
    mock_connection = Mock()
    mock_websocket.create_connection.return_value = mock_connection
    mock_connection.recv.side_effect = [
        """
        {
            "type": "data",
            "id": "123",
            "payload": {
                "data": {"test": "1"}
            }
        }
        """
    ]
    try:
        list(endpoint('query {test}'))
        raise Exception('should have failed')
    except ValueError as e:
        eq_(e.args[0], 'Unexpected data when waiting for connection ack')


@patch('sgqlc.endpoint.websocket.websocket')
def test_unexpected_ack_id(mock_websocket):
    'Test bad message id when waiting for ack'
    mock_connection = Mock()
    mock_websocket.create_connection.return_value = mock_connection
    mock_connection.recv.side_effect = [
        """
        {
            "type": "connection_ack",
            "id": "321",
            "payload": {
                "data": {"test": "1"}
            }
        }
        """
    ]
    try:
        list(endpoint('query {test}'))
        raise Exception('should have failed')
    except ValueError as e:
        eq_(e.args[0], 'Unexpected id 321 when waiting for connection ack')


@patch('sgqlc.endpoint.websocket.websocket')
def test_query_bad_message(mock_websocket):
    'Test bad message type when waiting for query'
    mock_connection = Mock()
    mock_websocket.create_connection.return_value = mock_connection
    mock_connection.recv.side_effect = [
        """
        {
            "type": "connection_ack",
            "id": "123"
        }
        """,
        """
        {
            "type": "error",
            "id": "123",
            "payload": {
                "data": {"test": ["1", "2"]}
            }
        }
        """,
    ]
    try:
        list(endpoint('query {test}'))
        raise Exception('should have failed')
    except ValueError as e:
        eq_(e.args[0].startswith('Unexpected message'), True)
        eq_(e.args[0].endswith('when waiting for query results'), True)


@patch('sgqlc.endpoint.websocket.websocket')
def test_query_bad_message_id(mock_websocket):
    'Test bad message id when waiting for query'
    mock_connection = Mock()
    mock_websocket.create_connection.return_value = mock_connection
    mock_connection.recv.side_effect = [
        """
        {
            "type": "connection_ack",
            "id": "123"
        }
        """,
        """
        {
            "type": "data",
            "id": "321",
            "payload": {
                "data": {"test": ["1", "2"]}
            }
        }
        """,
    ]
    try:
        list(endpoint('query {test}'))
        raise Exception('should have failed')
    except ValueError as e:
        eq_(e.args[0], 'Unexpected id 321 when waiting for query results')
