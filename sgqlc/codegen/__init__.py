'''
Generate SGQLC Code
===================

Downloading schema.json
-----------------------

The schema can be downloaded using :mod:`sgqlc.introspection`.


Generating Schema Types
-----------------------

While one can manually write the schema using :mod:`sgqlc.types`, it can
be a daunting task. This can be automated if the ``schema.json`` is available:

.. code-block:: shell

    sgqlc-codegen schema --docstrings schema.json my_schema.py

One may omit ``--docstrings`` to save space or speed up file loading
(however `Python's -OO/$PYTHONOPTIMIZE
<https://docs.python.org/3/using/cmdline.html#cmdoption-oo>`_ will
drop them).


Generating Operations
---------------------

If you're savvy enough to write GraphQL executable documents (aka "queries")
using their Domain Specific Language (DSL), or they exist somehow, they can
be used to generate :class:`sgqlc.operation.Operation` and can be used to
serialize and interpret results. The following command will use the
``schema.json``, the ``my_schema`` (generated in the previous section)
and the ``my_operations.gql`` with the GraphQL executable document to generate
the ``my_operations.py``. This file can then be imported and the functions
called to create the :class:`sgqlc.operation.Operation`.

.. code-block:: shell

    sgqlc-codegen operation \\
        --schema schema.json \\
        my_schema \\
        my_operations.py \\
        my_operations.gql


See examples:
 - `GitHub
   <https://github.com/profusion/sgqlc/blob/master/examples/github/update-operations.sh>`_
   defining a single parametrized (variables) query
   `ListIssues
   <https://github.com/profusion/sgqlc/blob/master/examples/github/sample_operations.gql>`_
   and generates
   `sample_operations.py
   <https://github.com/profusion/sgqlc/blob/master/examples/github/sample_operations.py>`_.
 - `Shopify
   <https://github.com/profusion/sgqlc/blob/master/examples/shopify/update-operations.sh>`_
   uses
   `shopify_operations.gql
   <https://github.com/profusion/sgqlc/blob/master/examples/shopify/shopify_operations.gql>`_
   defining all the operations, including fragments and variables, and outputs
   the SGQLC code. See the generated
   `shopify_operations.py
   <https://github.com/profusion/sgqlc/blob/master/examples/shopify/shopify_operations.py>`_.


:license: ISC
'''

__docformat__ = 'reStructuredText en'

import argparse
import sys

from . import schema
from . import operation


__all__ = ('SchemaCodeGen',)


SchemaCodeGen = schema.CodeGen


def get_arg_parse():
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

    return ap


def main():
    ap = get_arg_parse()

    # default to 'schema' for backward compatibility
    subparsers = ap._subparsers._group_actions[0]
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
