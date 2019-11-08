'''
Access GraphQL endpoints using Python
=====================================

This package provide the following modules:

 - :mod:`sgqlc.endpoint.base`: with abstract class
   :class:`sgqlc.endpoint.base.BaseEndpoint` and helpful logging
   utilities to transform errors into JSON objects.

 - :mod:`sgqlc.endpoint.http`: concrete
   :class:`sgqlc.endpoint.http.HTTPEndpoint` using
   :func:`urllib.request.urlopen()`.

 - :mod:`sgqlc.endpoint.requests`: concrete
   :class:`sgqlc.endpoint.requests.RequestsEndpoint` using
   :mod:`requests` .

:license: ISC
'''

__docformat__ = 'reStructuredText en'
