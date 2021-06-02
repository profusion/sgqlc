#!/bin/sh

sgqlc-codegen operation \
    --schema shopify_schema.json \
    shopify_schema \
    shopify_operations.py \
    shopify_operations.gql

python3 -c 'import shopify_operations' || exit 1
