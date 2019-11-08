=======================
Simple GraphQL Client
=======================

This package offers an easy-to-use GraphQL client. The source code is extensively documented,
so to get started, have a look at the following modules:

* Use :mod:`sgqlc.endpoint` to access GraphQL endpoints, notably :mod:`sgqlc.endpoint.http` provides :class:`HTTPEndpoint` that makes use of :mod:`urllib.request.urlopen()`.

* To declare GraphQL schema types as Python classes, use :mod:`sgqlc.types`. These type classes can then be used by :mod:`sgqlc.operation` to generate and interpret GraphQL queries.

* :mod:`sgqlc.types.datetime` provides bindings for :mod:`datetime` and ISO 8601, while :mod:`sgqlc.types.relay` exposes ``Node``, ``PageInfo`` and ``Connection`` types, useful for pagination.

Table of Contents
==================

.. toctree::

   sgqlc.types
   sgqlc.types.datetime
   sgqlc.types.relay
   sgqlc.operation
   sgqlc.endpoint
   sgqlc.endpoint.base
   sgqlc.endpoint.http
   sgqlc.endpoint.requests


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

:license: ISC
