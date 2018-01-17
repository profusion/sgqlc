`sgqlc` - Simple GraphQL Client
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Introduction
------------

This package offers easy to use `GraphQL <http://graphql.org>`_
client. It's composed by the following modules:

 - :mod:`sgqlc.types`: declare GraphQL in Python, base to generate and
   interpret queries. Submodule :mod:`sgqlc.types.datetime` will
   provide bindings for :mod:`datetime` and ISO 8601, while
   :mod:`sgqlc.types.relay` will expose ``Node``, ``PageInfo`` and
   ``Connection``.

 - :mod:`sgqlc.operation`: use declared types to generate and
   interpret queries.

 - :mod:`sgqlc.endpoint`: provide access to GraphQL endpoints, notably
   :mod:`sgqlc.endpoint.http` provides :class:`HTTPEndpoint` using
   :mod:`urllib.request.urlopen()`.



Installation
------------

Automatic::

    pip install sgqlc

From source using ``pip``::

    pip install .


Usage
-----

To reach a GraphQL endpoint using synchronous `HTTPEndpoint` with a
hand-written query (see more at ``examples/basic/http-endpoint.py``):

.. code-block:: python

   from sgqlc.endpoint.http import HTTPEndpoint

   url = 'http://server.com/graphql'
   headers = {'Authorization': 'bearer TOKEN'}

   query = 'query { ... }'
   variables = {'varName': 'value'}

   endpoint = HTTPEndpoint(url, headers)
   data = endpoint(query, variables)


However, writing GraphQL queries and later interpreting the results
may be cumbersome, that's solved with our ``sgqlc.types``, that is
usually paired with ``sgqlc.operation`` to generate queries and then
interpret results (see more at ``examples/basic/types.py``). The
example below matches a subset of `GitHub API v4
<https://developer.github.com/v4/query/>`_, in GraphQL syntax it would
be::

   query {
     repository(owner: "profusion", name: "sgqlc") {
       issues(first: 100) {
         nodes {
           number
           title
         }
       }
     }
   }

The output JSON object is:

.. code-block:: json

   {
     "data": {
       "repository": {
         "issues": {
           "nodes": [
             {"number": 1, "title": "..."},
             {"number": 2, "title": "..."}
           ]
         }
       }
     }
   }

.. code-block:: python

   from sgqlc.endpoint.http import HTTPEndpoint
   from sgqlc.types import Type, Field, list_of
   from sgqlc.types.relay import Connection, connection_args
   from sgqlc.operation import Operation

   # Declare types matching GitHub GraphQL schema:
   class Issue(Type):
       number = int
       title = str

   class IssueConnection(Connection):
       nodes = list_of(Issue)

   class Repository(Type):
       issues = Field(IssueConnection, args=connection_args())

   class Query(Type):  # GraphQL's root
       repository = Field(Repository, args={'owner': str, 'name': str})

   # Generate an operation on Query, selecting fields:
   op = Operation(Query)
   issues = op.repository(owner=owner, name=name).issues(first=100).nodes
   issues.number()
   issues.title()

   # Call the endpoint:
   data = endpoint(op)

   # Interpret results into native objects
   repo = (op + data).repository
   for issue in repo.issues.nodes:
       print(issue)


Authors
-------

  - `Gustavo Sverzut Barbieri <barbieri@profusion.mobi>`_


License
-------
`sgqlc` is licensed under the `ISC <https://opensource.org/licenses/ISC>`_.
