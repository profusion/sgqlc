import argparse
import sys

from . import schema
from . import operation


__all__ = ('SchemaCodeGen',)


SchemaCodeGen = schema.CodeGen


def main():
    ap = argparse.ArgumentParser(
        description='Generate sgqlc-based code',
    )
    subparsers = ap.add_subparsers(dest='command')

    sp = subparsers.add_parser(
        'schema',
        help='Generate sgqlc types using GraphQL introspection data',
    )
    sp.set_defaults(func=schema.handle_command)
    schema.add_arguments(sp)

    sp = subparsers.add_parser(
        'operation',
        help='Generate sgqlc operations using GraphQL (DSL)',
    )
    sp.set_defaults(func=operation.handle_command)
    operation.add_arguments(sp)

    # default to 'schema' for backward compatibility
    subcommands = subparsers.choices.keys()
    raw_args = list(sys.argv[1:])
    for i, arg in enumerate(raw_args):
        if arg.startswith('-'):
            continue
        elif arg not in subcommands:
            raw_args.insert(i, 'schema')
            sys.stderr.writelines((
                'WARNING: ', sys.argv[0],
                ' now requires a "command" specifier. Assuming "schema". '
                'Please update your usage as this automatic conversion '
                'will be removed in the future!\n'
            ))
        break

    args = ap.parse_args(raw_args)
    args.func(args)
