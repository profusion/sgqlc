#!/usr/bin/env python3

import argparse
import logging
import sys

from sgqlc.endpoint.http import HTTPEndpoint  # noqa: I900
from shopify_operations import Operations  # noqa: I900

logger = logging.getLogger(__name__)


def money_to_text(money):
    return '%(currency_code)s %(amount)s' % money


def price_range_to_text(price_range):
    min_range = money_to_text(price_range.min_variant_price)
    max_range = money_to_text(price_range.max_variant_price)
    if min_range == max_range:
        return min_range
    return '%s...%s' % (min_range, max_range)


def print_product(product):
    sys.stdout.write('''\
%(handle)s (%(total_inventory)s) - %(title)s
    %(description)s
    %(id)s
''' % product)
    sys.stdout.write('    Price: %s\n' %
                     (price_range_to_text(product.price_range_v2),))


ap = argparse.ArgumentParser(description='Shopify List Products')
ap.add_argument('shop_store', help='Shopify Store name')
ap.add_argument('token', help='X-Shopify-Access-Token to use')
ap.add_argument('--page-size', '-p',
                help='Page size to use, default=%(default)s',
                default=3,
                type=int)
ap.add_argument('--verbose', '-v',
                help='Increase verbosity',
                action='count',
                default=0)

args = ap.parse_args()

endpoint_loglevel = max(10, 40 - ((args.verbose - 3) * 10))
logfmt = '%(levelname)s: %(message)s'
if endpoint_loglevel < logging.ERROR:
    logfmt = '%(levelname)s:%(name)s: %(message)s'

logging.basicConfig(format=logfmt, level=max(10, 40 - (args.verbose * 10)))
HTTPEndpoint.logger.setLevel(endpoint_loglevel)

url = 'https://%s.myshopify.com/admin/api/2020-10/graphql.json' % (
    args.shop_store,
)
endpoint = HTTPEndpoint(url, {'X-Shopify-Access-Token': args.token})

page_size = args.page_size


op = Operations.query.initial_query

logger.info('Endpoint %s', endpoint)
logger.debug('Operation:\n%s', op)

d = endpoint(op, {'first': page_size})
errors = d.get('errors')
if errors:
    raise SystemExit(errors)

data = (op + d)
sys.stdout.write('Shop: %(name)s - %(url)s\n' % data.shop)
if data.shop.description:
    sys.stdout.write('   %s\n' % (data.shop.description,))

if not data.products.edges:
    sys.stdout.write('No products!\n')
    raise SystemExit()


op = Operations.query.load_products
while data.products.page_info.has_next_page:
    # NOTE: Shopify doesn't expose page_info.end_cursor,
    # then we must get the last one:
    last_edge = data.products.edges[-1]
    after = last_edge.cursor

    logger.info('Downloading next page after: %s', after)
    logger.debug('Operation:\n%s', op)

    d = endpoint(op, {'first': page_size, 'after': after})
    errors = d.get('errors')
    if errors:
        raise SystemExit(errors)

    data.products += (op + d).products

sys.stdout.write('Found %s products:\n' % len(data.products.edges))
for edge in data.products.edges:
    print_product(edge.node)
