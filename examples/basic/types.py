#!/usr/bin/env python3

import sys
from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.types import Type, Field, list_of
from sgqlc.types.relay import Connection, connection_args
from sgqlc.operation import Operation


# Declare types matching GitHub GraphQL schema:
class Issue(Type):
    number = int
    title = str


class IssueConnection(Connection):
    nodes = list_of(Issue)


class Repository(Type):
    issues = Field(IssueConnection, args=connection_args())


class Query(Type):  # GraphQL's root
    repository = Field(Repository, args={'owner': str, 'name': str})


try:
    token, repo = sys.argv[1:]
except ValueError:
    raise SystemExit('Usage: <token> <team/repo>')

url = 'https://api.github.com/graphql'
headers = {
    'Authorization': 'bearer ' + token,
}

endpoint = HTTPEndpoint(url, headers)

owner, name = repo.split('/', 1)

# Generate an operation on Query, selecting fields:
op = Operation(Query)
issues = op.repository(owner=owner, name=name).issues(first=100).nodes
issues.number()
issues.title()

# Call the endpoint:
data = endpoint(op)

# Interpret results into native objects
repo = (op + data).repository
for issue in repo.issues.nodes:
    print(issue)
