#!/bin/sh

if [ -z "$GH_TOKEN" ]; then
    echo "please export GH_TOKEN with your GitHub API token" >&2
    echo "see: https://github.com/settings/tokens" >&2
    exit 1
fi

python3 \
    -m sgqlc.introspection \
    --exclude-deprecated \
    --exclude-description \
    -H "Authorization: bearer ${GH_TOKEN}" \
    https://api.github.com/graphql \
    github_schema.json || exit 1

sgqlc-codegen github_schema.json github_schema.py
