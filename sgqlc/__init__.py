'''
This package offers an easy-to-use GraphQL client. The source code is
extensively documented, so to get started, have a look at the following
modules:

* Use :mod:`sgqlc.endpoint` to access GraphQL endpoints, notably
  :mod:`sgqlc.endpoint.http` provides :class:`HTTPEndpoint` that makes
  use of :mod:`urllib.request.urlopen()`.

* To declare GraphQL schema types as Python classes, use :mod:`sgqlc.types`.

* These type classes can then be used by :mod:`sgqlc.operation` to generate
  and interpret GraphQL queries.

* :mod:`sgqlc.codegen` offers code generation to help using :mod:`sgqlc.types`
  from schema introspection results (``schema.json``) and
  :mod:`sgqlc.operation` using GraphQL Domain Specific Language (DSL)
  executable documents.

* :mod:`sgqlc.types.datetime` provides bindings for :mod:`datetime` and
  ISO 8601, while :mod:`sgqlc.types.relay` exposes ``Node``, ``PageInfo`` and
  ``Connection`` types, useful for pagination.

:license: ISC
'''

__docformat__ = 'reStructuredText en'
__version__ = '14.0'
