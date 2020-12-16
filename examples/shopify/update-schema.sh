#!/bin/sh

SHOP_STORE=${SHOP_STORE:-sgqlc-test}
if [ -z "$SHOP_TOKEN" ]; then
    echo "please export SHOP_TOKEN with your Shopify X-Shopify-Access-Token" >&2
    echo "See https://shopify.dev/docs/admin-api/graphql/getting-started#authentication" >&2
    exit 1
fi

python3 \
    -m sgqlc.introspection \
    --exclude-deprecated \
    --exclude-description \
    -H "X-Shopify-Access-Token: ${SHOP_TOKEN}" \
    https://${SHOP_STORE}.myshopify.com/admin/api/2020-10/graphql.json \
    shopify_schema.json || exit 1

sgqlc-codegen schema shopify_schema.json shopify_schema.py
