#!/bin/sh

sgqlc-codegen operation \
    --schema github_schema.json \
    github_schema \
    sample_operations.py \
    sample_operations.gql

python3 -c 'import sample_operations' || exit 1
