#!/usr/bin/env python3

import os
import sys
from sgqlc.endpoint.http import HTTPEndpoint
from sample_operations import Operations  # noqa: I900

endpoint = HTTPEndpoint(
    'https://api.github.com/graphql',
    {
        'Authorization': 'bearer ' + os.environ['GH_TOKEN'],
    },
)


owner, name = sys.argv[1:3]

op = Operations.query.list_issues

# you can print the resulting GraphQL
print(op)  # noqa: T001

# Call the endpoint:
data = endpoint(op, {'owner': owner, 'name': name})

# Interpret results into native objects
repo = (op + data).repository
for issue in repo.issues.nodes:
    print(issue)  # noqa: T001
