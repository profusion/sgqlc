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

 - :mod:`sgqlc.endpoint.websocket`: concrete
   :class:`sgqlc.endpoint.websocket.WebSocketEndpoint` using
   :func:`websocket._core.create_connection`.

Unless otherwise stated the endpoints follow a pattern:
 - construct the endpoint giving constants such as address, timeout...
 - call the endpoint given an operation and variables

The given ``variables`` must be a **plain JSON-serializeable object**
(dict with string keys and values being one of dict, list, tuple, str, int,
float, bool, None... -- :func:`json.dumps` is used)
and the keys must **match exactly** the variable names (no name conversion
is done, no dollar-sign prefix ``$`` should be used).

Example using :class:`sgqlc.endpoint.http.HTTPEndpoint`:

.. literalinclude:: ../../examples/basic/01_http_endpoint.py
   :language: python

See `more examples <https://github.com/profusion/sgqlc/tree/master/examples>`_.

:license: ISC
'''

__docformat__ = 'reStructuredText en'
