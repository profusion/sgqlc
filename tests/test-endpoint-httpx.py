import json

import httpx

from sgqlc.endpoint.httpx import HTTPXEndpoint
from sgqlc.types import Schema, Type
from sgqlc.operation import Operation

test_url = 'http://some-server.com/graphql'

extra_accept_header = ', '.join(
    [
        'application/json; charset=utf-8',
        'application/vnd.xyz.feature-flag+json',
    ]
)

graphql_query = '''
query GitHubRepoIssues($repoOwner: String!, $repoName: String!) {
  repository(owner: $repoOwner, name: $repoName) {
    issues(first: 100) {
      nodes {
        number
        title
      }
    }
  }
}
'''

graphql_headers_ok = {
    'Content-Type': 'application/json; charset=utf8',
    'X-Ratelimit-Limit': '1000',
}

graphql_headers_gzip = {
    'Content-Type': 'application/json; charset=utf8',
    'X-Ratelimit-Limit': '1000',
    'Content-Encoding': 'gzip',
}


graphql_response_ok = {
    'headers': {
        'Content-Type': 'application/json; charset=utf8',
        'X-Ratelimit-Limit': '1000',
    },
    'data': {
        'repository': {
            'issues': {
                'nodes': [{'number': 1, 'title': 'unit tests: sgqlc.types'}]
            }
        }
    },
}

graphql_response_error = {
    'headers': {
        'Content-Type': 'application/json; charset=utf8',
        'X-Ratelimit-Limit': '1000',
    },
    'errors': [
        {
            'message': 'Server Reported Error',
            'locations': [{'line': 1, 'column': 1}],
        },
        {'message': 'Other Message', 'path': ['repository', 'issues']},
    ],
}

graphql_response_json_error = b'''
{
  "data": {
'''

# -- Test Helpers --


def get_json_exception(s):
    try:
        json.loads(s)
        return None
    except json.JSONDecodeError as e:
        return e


def check_request_headers_(req, headers, name):
    if not headers:
        return
    if isinstance(headers, dict):
        headers = headers.items()
    for k, v in headers:
        g = req.headers[k]
        assert g == v, 'Failed {} header {}: {!r} != {!r}'.format(
            name, k, v, g
        )


def check_request_headers(req, base_headers, extra_headers):
    if extra_headers and 'Accept' in extra_headers:
        accept_header = extra_accept_header
    else:
        accept_header = 'application/json; charset=utf-8'
    assert req.headers['Accept'] == accept_header
    if req.method == 'POST':
        assert req.headers['Content-type'] == 'application/json'
    check_request_headers_(req, base_headers, 'base')
    check_request_headers_(req, extra_headers, 'extra')


def check_request_variables(req, variables):
    if req.method == 'POST':
        post_data = json.loads(req.content)
        received = post_data.get('variables')
    else:
        received = json.loads(req.url.params.get('variables', 'null'))

    assert received == variables


def check_request_operation_name(req, operation_name):
    if req.method == 'POST':
        post_data = json.loads(req.content)
        received = post_data.get('operationName')
    else:
        received = req.url.params.get('operationName')

    assert received == operation_name


def check_request_query(req, query):
    if req.method == 'POST':
        post_data = json.loads(req.content)
        received = post_data.get('query')
    else:
        received = req.url.params.get('query')

    if isinstance(query, bytes):
        query = query.decode('utf-8')

    assert received == query


def check_respx_route(
    route,
    timeout=None,
    base_headers=None,
    extra_headers=None,
    variables=None,
    operation_name=None,
    query=None,  # defaults to `graphql_query`
):
    assert route.called
    req = route.calls.last.request
    check_request_headers(req, base_headers, extra_headers)
    check_request_variables(req, variables)
    check_request_operation_name(req, operation_name)
    check_request_query(req, query or graphql_query)

    assert route.calls.last.request.extensions['timeout']['connect'] == timeout
    assert route.calls.last.request.extensions['timeout']['read'] == timeout
    assert route.calls.last.request.extensions['timeout']['write'] == timeout
    assert route.calls.last.request.extensions['timeout']['pool'] == timeout


# -- Actual Tests --


def test_basic(respx_mock):
    'Test if basic usage with only essential parameters works'

    route = respx_mock.route(name='graphql', method='POST', url=test_url).mock(
        return_value=httpx.Response(
            200, json=graphql_response_ok, headers=graphql_headers_ok
        )
    )

    endpoint = HTTPXEndpoint(test_url)
    data = endpoint(graphql_query)
    assert data == graphql_response_ok

    check_respx_route(route)
    assert str(endpoint) == (
        'HTTPXEndpoint(url={}, '.format(test_url)
        + 'base_headers={}, timeout=None, method=POST)'
    )


async def test_basic_async(respx_mock):
    'Test if basic usage with an async client'

    route = respx_mock.route(name='graphql', method='POST', url=test_url).mock(
        return_value=httpx.Response(
            200, json=graphql_response_ok, headers=graphql_headers_ok
        )
    )

    endpoint = HTTPXEndpoint(test_url, client=httpx.AsyncClient())
    data = await endpoint(graphql_query)
    assert data == graphql_response_ok
    check_respx_route(route)


def test_basic_bytes_query(respx_mock):
    'Test if query with type bytes works'

    route = respx_mock.route(name='graphql', method='POST', url=test_url).mock(
        return_value=httpx.Response(
            200, json=graphql_response_ok, headers=graphql_headers_ok
        )
    )

    endpoint = HTTPXEndpoint(test_url)
    data = endpoint(graphql_query.encode('utf-8'))
    assert data == graphql_response_ok
    check_respx_route(route)


def test_basic_operation_query(respx_mock):
    'Test if query with type sgqlc.operation.Operation() works'

    route = respx_mock.route(name='graphql', method='POST', url=test_url).mock(
        return_value=httpx.Response(
            200, json=graphql_response_ok, headers=graphql_headers_ok
        )
    )

    schema = Schema()

    # MyType and Query may be declared if doctests were processed by pytest
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

    endpoint = HTTPXEndpoint(test_url)
    data = endpoint(op)
    assert data == graphql_response_ok
    check_respx_route(route, query=bytes(op))


def test_headers(respx_mock):
    'Test if all headers are passed'

    route = respx_mock.route(name='graphql', method='POST', url=test_url).mock(
        return_value=httpx.Response(
            200, json=graphql_response_ok, headers=graphql_headers_ok
        )
    )

    base_headers = {
        'Xpto': 'abc',
    }
    extra_headers = {
        'Extra': '123',
        'Accept': extra_accept_header,
    }

    endpoint = HTTPXEndpoint(test_url, base_headers=base_headers)
    data = endpoint(graphql_query, extra_headers=extra_headers)
    assert data == graphql_response_ok
    check_respx_route(
        route, base_headers=base_headers, extra_headers=extra_headers
    )


def test_default_timeout(respx_mock):
    'Test if default timeout is respected'

    route = respx_mock.route(name='graphql', method='POST', url=test_url).mock(
        return_value=httpx.Response(
            200, json=graphql_response_ok, headers=graphql_headers_ok
        )
    )

    timeout = 123

    endpoint = HTTPXEndpoint(test_url, timeout=timeout)
    data = endpoint(graphql_query)
    assert data == graphql_response_ok
    check_respx_route(route, timeout=timeout)


def test_call_timeout(respx_mock):
    'Test if call timeout takes precedence over default'

    route = respx_mock.route(name='graphql', method='POST', url=test_url).mock(
        return_value=httpx.Response(
            200, json=graphql_response_ok, headers=graphql_headers_ok
        )
    )

    timeout = 123

    endpoint = HTTPXEndpoint(test_url, timeout=1)
    data = endpoint(graphql_query, timeout=timeout)
    assert data == graphql_response_ok
    check_respx_route(route, timeout=timeout)


def test_variables(respx_mock):
    'Test if variables are passed to server'

    route = respx_mock.route(name='graphql', method='POST', url=test_url).mock(
        return_value=httpx.Response(
            200, json=graphql_response_ok, headers=graphql_headers_ok
        )
    )

    variables = {'repoOwner': 'owner', 'repoName': 'name'}

    endpoint = HTTPXEndpoint(test_url)
    data = endpoint(graphql_query, variables)
    assert data == graphql_response_ok
    check_respx_route(route, variables=variables)


def test_operation_name(respx_mock):
    'Test if operation name is passed to server'

    route = respx_mock.route(name='graphql', method='POST', url=test_url).mock(
        return_value=httpx.Response(
            200, json=graphql_response_ok, headers=graphql_headers_ok
        )
    )

    operation_name = 'xpto'

    endpoint = HTTPXEndpoint(test_url)
    data = endpoint(graphql_query, operation_name=operation_name)
    assert data == graphql_response_ok
    check_respx_route(route, operation_name=operation_name)


def test_json_error(respx_mock):
    'Test if broken server responses (invalid JSON) is handled'

    route = respx_mock.route(name='graphql', method='POST', url=test_url).mock(
        return_value=httpx.Response(
            200,
            content=graphql_response_json_error,
            headers=graphql_headers_ok,
        )
    )

    endpoint = HTTPXEndpoint(test_url)
    data = endpoint(graphql_query)

    exc = get_json_exception(graphql_response_json_error)
    got_exc = data['errors'][0].pop('exception')
    assert isinstance(
        got_exc, json.JSONDecodeError
    ), '{} is not json.JSONDecodeError'.format(type(got_exc))

    assert data == {
        'errors': [
            {
                'message': str(exc),
                'body': graphql_response_json_error.decode('utf-8'),
            }
        ],
        'data': None,
    }
    check_respx_route(route)


def test_get(respx_mock):
    'Test if HTTP method GET request works'

    route = respx_mock.route(name='graphql', method='GET', url=test_url).mock(
        return_value=httpx.Response(
            200, json=graphql_response_ok, headers=graphql_headers_ok
        )
    )

    base_headers = {
        'Xpto': 'abc',
    }
    extra_headers = {
        'Extra': '123',
        'Accept': extra_accept_header,
    }
    variables = {'repoOwner': 'owner', 'repoName': 'name'}
    operation_name = 'xpto'

    endpoint = HTTPXEndpoint(test_url, base_headers=base_headers, method='GET')
    data = endpoint(
        graphql_query,
        extra_headers=extra_headers,
        variables=variables,
        operation_name=operation_name,
    )
    assert data == graphql_response_ok
    check_respx_route(
        route,
        base_headers=base_headers,
        extra_headers=extra_headers,
        variables=variables,
        operation_name=operation_name,
    )
    assert str(endpoint) == (
        'HTTPXEndpoint(url={}, '.format(test_url)
        + 'base_headers={}, '.format(base_headers)
        + 'timeout=None, method=GET)'
    )


def test_server_reported_error(respx_mock):
    'Test if GraphQL errors reported with HTTP 200 is handled properly'

    route = respx_mock.route(name='graphql', method='POST', url=test_url).mock(
        return_value=httpx.Response(
            200, json=graphql_response_error, headers=graphql_headers_ok
        )
    )

    endpoint = HTTPXEndpoint(test_url)
    data = endpoint(graphql_query)
    assert data == graphql_response_error
    check_respx_route(route)


def test_server_http_error(respx_mock):
    'Test if HTTP error without JSON payload is handled'

    route = respx_mock.route(name='graphql', method='POST', url=test_url).mock(
        return_value=httpx.Response(
            500, content=b'xpto', headers={'Xpto': 'abc'}
        )
    )

    endpoint = HTTPXEndpoint(test_url)
    data = endpoint(graphql_query)

    got_exc = data['errors'][0].pop('exception')
    assert isinstance(
        got_exc, httpx.HTTPStatusError
    ), '{} is not httpx.HTTPStatusError'.format(type(got_exc))

    assert data == {
        'errors': [
            {
                'message': 'Server error \'500 Internal Server Error\' for url'
                ' \'http://some-server.com/graphql\'\nFor more information che'
                'ck: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/'
                '500',
                'status': 500,
                'headers': {'xpto': 'abc', 'content-length': '4'},
                'body': 'xpto',
            }
        ],
        'data': None,
    }
    check_respx_route(route)


async def test_server_http_error_async(respx_mock):
    'Test if HTTP error without JSON payload is handled'

    route = respx_mock.route(name='graphql', method='POST', url=test_url).mock(
        return_value=httpx.Response(
            500, content=b'xpto', headers={'Xpto': 'abc'}
        )
    )

    endpoint = HTTPXEndpoint(test_url, client=httpx.AsyncClient())
    data = await endpoint(graphql_query)

    got_exc = data['errors'][0].pop('exception')
    assert isinstance(
        got_exc, httpx.HTTPStatusError
    ), '{} is not httpx.HTTPStatusError'.format(type(got_exc))

    assert data == {
        'errors': [
            {
                'message': 'Server error \'500 Internal Server Error\' for url'
                ' \'http://some-server.com/graphql\'\nFor more information che'
                'ck: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/'
                '500',
                'status': 500,
                'headers': {'xpto': 'abc', 'content-length': '4'},
                'body': 'xpto',
            }
        ],
        'data': None,
    }
    check_respx_route(route)


def test_server_http_non_conforming_json(respx_mock):
    'Test if HTTP error that is NOT conforming to GraphQL payload is handled'

    content = '{"message": "xpto"}'
    content_length = len(content)

    req = httpx.Request('POST', test_url)
    res = httpx.Response(
        500,
        content=content,
        headers={
            'content-type': 'application/json',
            'content-length': str(content_length),
        },
        request=req,
    )
    exp_exc = None  # placeholder, will always be set in the handler below
    try:
        res.raise_for_status()
    except httpx.HTTPStatusError as e:
        exp_exc = e

    route = respx_mock.route(name='graphql', method='POST', url=test_url).mock(
        return_value=res,
    )

    endpoint = HTTPXEndpoint(test_url)
    data = endpoint(graphql_query)

    got_exc = data['errors'][0].pop('exception')
    assert isinstance(
        got_exc, httpx.HTTPStatusError
    ), '{} is not httpx.HTTPStatusError'.format(type(got_exc))

    assert data == {
        'errors': [
            {
                'message': str(exp_exc),
                'status': 500,
                'headers': {
                    'content-type': 'application/json',
                    'content-length': str(content_length),
                },
                'body': content,
            }
        ],
        'data': None,
    }
    check_respx_route(route)


def test_server_error_broken_json(respx_mock):
    'Test if HTTP error with broken JSON payload is handled'

    route = respx_mock.route(name='graphql', method='POST', url=test_url).mock(
        return_value=httpx.Response(
            500, content=b'xpto', headers={'Content-Type': 'application/json'}
        )
    )

    endpoint = HTTPXEndpoint(test_url)
    data = endpoint(graphql_query)
    got_exc = data['errors'][0].pop('exception')
    assert isinstance(
        got_exc, json.JSONDecodeError
    ), '{} is not json.JSONDecodeError'.format(type(got_exc))

    assert data == {
        'errors': [
            {
                'message': str(got_exc),
                'body': 'xpto',
            }
        ],
        'data': None,
    }
    check_respx_route(route)


def test_server_http_graphql_error(respx_mock):
    'Test if HTTP error that IS conforming to GraphQL payload is handled'

    route = respx_mock.route(name='graphql', method='POST', url=test_url).mock(
        return_value=httpx.Response(500, json=graphql_response_error)
    )

    endpoint = HTTPXEndpoint(test_url)
    data = endpoint(graphql_query)

    expected_data = graphql_response_error
    expected_data.update(
        {
            'status': 500,
            'headers': {
                'content-type': 'application/json',
                'content-length': '230',
            },
        }
    )

    got_exc = data.pop('exception')
    assert isinstance(
        got_exc, httpx.HTTPStatusError
    ), '{} is not httpx.HTTPStatusError'.format(type(got_exc))

    assert data == expected_data
    check_respx_route(route)


def test_server_http_single_error(respx_mock):
    'Test if HTTP error that a single JSON error string is handled'

    route = respx_mock.route(name='graphql', method='POST', url=test_url).mock(
        return_value=httpx.Response(500, json={'errors': 'a string'})
    )

    endpoint = HTTPXEndpoint(test_url)
    data = endpoint(graphql_query)

    expected_data = {'errors': [{'message': 'a string'}]}
    expected_data.update(
        {
            'status': 500,
            'headers': {
                'content-type': 'application/json',
                'content-length': '21',
            },
        }
    )

    got_exc = data.pop('exception')
    assert isinstance(
        got_exc, httpx.HTTPStatusError
    ), '{} is not httpx.HTTPStatusError'.format(type(got_exc))

    assert data == expected_data
    check_respx_route(route)


def test_server_http_error_string_list(respx_mock):
    'Test if HTTP error that a JSON error string list is handled'

    route = respx_mock.route(name='graphql', method='POST', url=test_url).mock(
        return_value=httpx.Response(500, json={'errors': ['a', 'b']})
    )

    endpoint = HTTPXEndpoint(test_url)
    data = endpoint(graphql_query)

    expected_data = {'errors': [{'message': 'a'}, {'message': 'b'}]}
    expected_data.update(
        {
            'status': 500,
            'headers': {
                'content-type': 'application/json',
                'content-length': '20',
            },
        }
    )

    got_exc = data.pop('exception')
    assert isinstance(
        got_exc, httpx.HTTPStatusError
    ), '{} is not httpx.HTTPStatusError'.format(type(got_exc))

    assert data == expected_data
    check_respx_route(route)


def test_server_http_error_list_message(respx_mock):
    'Test if HTTP error that a JSON error with messages being a list'

    route = respx_mock.route(name='graphql', method='POST', url=test_url).mock(
        return_value=httpx.Response(
            500, json={'errors': [{'message': [1, 2]}]}
        )
    )

    endpoint = HTTPXEndpoint(test_url)
    data = endpoint(graphql_query)

    expected_data = {'errors': [{'message': '[1, 2]'}]}
    expected_data.update(
        {
            'status': 500,
            'headers': {
                'content-type': 'application/json',
                'content-length': '30',
            },
        }
    )

    got_exc = data.pop('exception')
    assert isinstance(
        got_exc, httpx.HTTPStatusError
    ), '{} is not httpx.HTTPStatusError'.format(type(got_exc))

    assert data == expected_data
    check_respx_route(route)
