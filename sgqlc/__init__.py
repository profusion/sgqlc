'''
sgqlc - Simple GraphQL Client
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This package provide the following modules:

 - :mod:`sgqlc.types`: declare GraphQL in Python, base to generate and
   interpret queries. Submodule :mod:`sgqlc.types.datetime` will
   provide bindings for :mod:`datetime` and ISO 8601, while
   :mod:`sgqlc.types.relay` will expose ``Node``, ``PageInfo`` and
   ``Connection``.

 - :mod:`sgqlc.operation`: use declared types to generate and
   interpret queries.

 - :mod:`sgqlc.endpoint`: provide access to GraphQL endpoints, notably
   :mod:`sgqlc.endpoint.http` provides
   :class:`sgqlc.endpoint.http.HTTPEndpoint` using
   :func:`urllib.request.urlopen()`.

:license: ISC
'''

__docformat__ = 'reStructuredText en'
