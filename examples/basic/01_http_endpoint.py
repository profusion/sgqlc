#!/usr/bin/env python3

import sys
import json
from sgqlc.endpoint.http import HTTPEndpoint

try:
    token, repo = sys.argv[1:]
except ValueError:
    raise SystemExit('Usage: <token> <team/repo>')

query = '''
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

owner, name = repo.split('/', 1)
variables = {
    'repoOwner': owner,
    'repoName': name,
}

url = 'https://api.github.com/graphql'
headers = {
    'Authorization': 'bearer ' + token,
}

endpoint = HTTPEndpoint(url, headers)
data = endpoint(query, variables)

json.dump(data, sys.stdout, sort_keys=True, indent=2, default=str)
