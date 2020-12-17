#!/bin/sh

sgqlc-codegen operation \
    --schema github_schema.json \
    github_schema \
    sample_operations.py \
    sample_operations.gql
