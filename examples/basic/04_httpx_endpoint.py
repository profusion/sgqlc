#!/usr/bin/env python3

import sys
import json
import httpx
import asyncio
from sgqlc.endpoint.httpx import HTTPXEndpoint


async def main():
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

    endpoint = HTTPXEndpoint(url, headers, client=httpx.AsyncClient())
    data = await endpoint(query, variables)

    json.dump(data, sys.stdout, sort_keys=True, indent=2, default=str)


asyncio.run(main())
