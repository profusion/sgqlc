#!/usr/bin/env python3

import json
import logging
import argparse
import sys

from ..endpoint.http import HTTPEndpoint
from . import query, variables


def tuple_arg(s):
    p = s.split('=', 1)
    if len(p) == 2:
        return p
    return s.split(':', 1)


def get_arg_parse():
    ap = argparse.ArgumentParser(
        description='Introspect a GraphQL endpoint using HTTP',
    )

    # Generic options to access the GraphQL API
    ap.add_argument('url', help='GraphQL endpoint address.')
    ap.add_argument('outfile', help='Where to write json. Default=stdout',
                    type=argparse.FileType('w'),
                    default=sys.stdout, nargs='?')

    ap.add_argument('--exclude-deprecated', action='store_true',
                    help=('If given, will exclude deprecated fields and '
                          'enumeration values.'),
                    default=False)
    ap.add_argument('--exclude-description', action='store_true',
                    help='If given, will exclude description (documentation).',
                    default=False)

    ap.add_argument('--header', '-H', action='append', type=tuple_arg,
                    help=('NAME=VALUE HTTP header to send. '
                          'Example: "Authorization: bearer ${token}"'),
                    default=[])
    ap.add_argument('--timeout', '-t', type=float, default=None,
                    help='Request timeout, in seconds.')
    ap.add_argument('--verbose', '-v',
                    help='Increase verbosity',
                    action='count',
                    default=0)

    return ap


if __name__ == '__main__':
    ap = get_arg_parse()
    args = ap.parse_args()

    logfmt = '%(levelname)s: %(message)s'
    logging.basicConfig(format=logfmt, level=max(10, 40 - (args.verbose * 10)))

    endpoint = HTTPEndpoint(args.url, dict(args.header), args.timeout)
    data = endpoint(query, variables(
        include_description=not args.exclude_description,
        include_deprecated=not args.exclude_deprecated,
    ))

    json.dump(data, args.outfile, sort_keys=True, indent=2, default=str)
    sys.stdout.write('\n')
    if data.get('errors'):
        sys.exit(1)
