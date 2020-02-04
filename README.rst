`sgqlc` - Simple GraphQL Client
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://travis-ci.com/profusion/sgqlc.svg?branch=master
    :target: https://travis-ci.com/profusion/sgqlc

.. image:: https://coveralls.io/repos/github/profusion/sgqlc/badge.svg?branch=master
    :target: https://coveralls.io/github/profusion/sgqlc?branch=master

Introduction
------------

This package offers an easy to use `GraphQL <http://graphql.org>`_
client. It's composed of the following modules:

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


What's GraphQL?
===============

Straight from http://graphql.org:

   **A query language for your API**

   GraphQL is a query language for APIs and a runtime for fulfilling
   those queries with your existing data. GraphQL provides a complete
   and understandable description of the data in your API, gives
   clients the power to ask for exactly what they need and nothing
   more, makes it easier to evolve APIs over time, and enables
   powerful developer tools.

It was created by Facebook based on their problems and solutions using
`REST <https://en.wikipedia.org/wiki/Representational_state_transfer>`_
to develop applications to consume their APIs. It was publicly
announced at
`React.js Conf 2015 <https://reactjs.org/blog/2015/02/20/introducing-relay-and-graphql.html>`_
and started to gain traction since then. Right now there are big names
transitioning from REST to GraphQL:
`Yelp <https://www.yelp.com/developers/graphql/guides/intro>`_
`Shopify <https://help.shopify.com/api/storefront-api/graphql>`_
and `GitHub <https://developer.github.com/v4/>`_, that did an
excellent
`post <https://githubengineering.com/the-github-graphql-api/>`_
to explain why they changed.

A short list of advantages over REST:

- Built-in schema, with documentation, strong typing and
  introspection. There is no need to use
  `Swagger <https://swagger.io>`_ or any other external tools to play
  with it. Actually GraphQL provides a standard in-browser IDE for
  exploring GraphQL endpoints: https://github.com/graphql/graphiql;

- Only the fields that you want. The queries must explicitly select which
  fields are required, and that's all you're getting. If more fields
  are added to the type, they **won't break** the API, since the new
  fields won't be returned to old clients, as they didn't ask for such
  fields. This makes much easier to keep APIs stable and **avoids
  versioning**. Standard REST usually delivers all available fields in
  the results, and when new fields are to be included, a new API
  version is added (reflected in the URL path, or in an HTTP header);

- All data in one request. Instead of navigating hypermedia-driven
  RESTful services, like  discovering new ``"_links": {"href"...`` and
  executing a new HTTP request, with GraphQL you specify nested
  queries and let the whole navigation be done by the server. This
  reduces latency **a lot**;

- The resulting JSON object matches the given query exactly; if
  you requested ``{ parent { child { info } } }``, you're going to
  receive the JSON object ``{"parent": {"child": {"info": value }}}``.

From GitHub's
`Migrating from REST to GraphQL <https://developer.github.com/v4/guides/migrating-from-rest/>`_
one can see these in real life::

   $ curl -v https://api.github.com/orgs/github/members
   [
     {
       "login": "...",
       "id": 1234,
       "avatar_url": "https://avatars3.githubusercontent.com/u/...",
       "gravatar_id": "",
       "url": "https://api.github.com/users/...",
       "html_url": "https://github.com/...",
       "followers_url": "https://api.github.com/users/.../followers",
       "following_url": "https://api.github.com/users/.../following{/other_user}",
       "gists_url": "https://api.github.com/users/.../gists{/gist_id}",
       "starred_url": "https://api.github.com/users/.../starred{/owner}{/repo}",
       "subscriptions_url": "https://api.github.com/users/.../subscriptions",
       "organizations_url": "https://api.github.com/users/.../orgs",
       "repos_url": "https://api.github.com/users/.../repos",
       "events_url": "https://api.github.com/users/.../events{/privacy}",
       "received_events_url": "https://api.github.com/users/.../received_events",
       "type": "User",
       "site_admin": true
     },
     ...
   ]

brings the whole set of member information, however you just want name
and avatar URL::

   query {
     organization(login:"github") { # select the organization
       members(first: 100) {        # then select the organization's members
         edges {  # edges + node: convention for paginated queries
           node {
             name
             avatarUrl
           }
         }
       }
     }
   }

Likewise, instead of 4 HTTP requests::

   curl -v https://api.github.com/repos/profusion/sgqlc/pulls/9
   curl -v https://api.github.com/repos/profusion/sgqlc/pulls/9/commits
   curl -v https://api.github.com/repos/profusion/sgqlc/issues/9/comments
   curl -v https://api.github.com/repos/profusion/sgqlc/pulls/9/reviews

A single GraphQL query brings all the needed information, and just the
needed information::

   query {
     repository(owner: "profusion", name: "sgqlc") {
       pullRequest(number: 9) {
         commits(first: 10) { # commits of profusion/sgqlc PR #9
           edges {
             node { commit { oid, message } }
           }
         }
         comments(first: 10) { # comments of profusion/sgqlc PR #9
           edges {
             node {
               body
               author { login }
             }
           }
         }
         reviews(first: 10) { # reviews of profusion/sgqlc/ PR #9
           edges { node { state } }
         }
       }
     }
   }


Motivation to create `sgqlc`
============================

As seen above, writing GraphQL queries is very easy, and it is equally easy to
interpret the results. So **what was the rationale to create sgqlc?**

- GraphQL has its domain-specific language (DSL), and mixing two
  languages is always painful, as seen with SQL + Python, HTML +
  Python... Being able to write just Python in Python is much
  better. Not to say that GraphQL naming convention is closer to
  Java/JavaScript, using ``aNameFormat`` instead of Python's
  ``a_name_format``.

- Navigating dict-of-stuff is a bit painful:
  ``d["repository"]["pullRequest"]["commits"]["edges"]["node"]``,
  since these are valid Python identifiers, we better write:
  ``repository.pull_request.commits.edges.node``.

- Handling new ``scalar`` types. GraphQL allows one to define new scalar
  types, such as ``Date``, ``Time`` and ``DateTime``. Often these are
  serialized as ISO 8601 strings and the user must parse them in their
  application. We offer ``sgqlc.types.datetime`` to automatically
  generate :class:`datetime.date`, :class:`datetime.time` and
  :class:`datetime.datetime`.

- Make it easy to write dynamic queries, including nested. As seen,
  GraphQL can be used to fetch lots of information in one go; however
  if what you need (arguments and fields) changes based on some
  variable, such as user input or cached data, then you need to
  concatenate strings to compose the final query. This can be error
  prone and servers may block you due to invalid queries. Some tools
  "solve" this by parsing the query locally before sending it to
  server. However usually the indentation is screwed and reviewing it
  is painful. We change that approach: use
  :class:`sgqlc.operation.Operation` and it will always generate valid
  queries, which can be printed out and properly indented. Bonus point
  is that it can be used to later interpret the JSON results into native
  Python objects.

- Usability improvements whenever needed. For instance
  `Relay <https://facebook.github.io/relay/>`_ published their
  `Cursor Connections Specification <https://facebook.github.io/relay/graphql/connections.htm>`_
  and its widely used. To load more data, you need to extend the
  previous data with newly fetched information, updating not only the
  nodes and edges, but also page information. This is done
  automatically by :class:`sgqlc.types.relay.Connection`.

Future plans include generating the Python classes from the GraphQL
schema, which can be automatically fetched from an endpoint using
the introspection query.

Installation
------------

Automatic::

    pip install sgqlc

From source using ``pip``::

    pip install .


Usage
-----

To reach a GraphQL endpoint using synchronous `HTTPEndpoint` with a
hand-written query (see more at ``examples/basic/01_http_endpoint.py``):

.. code-block:: python

   from sgqlc.endpoint.http import HTTPEndpoint

   url = 'http://server.com/graphql'
   headers = {'Authorization': 'bearer TOKEN'}

   query = 'query { ... }'
   variables = {'varName': 'value'}

   endpoint = HTTPEndpoint(url, headers)
   data = endpoint(query, variables)


However, writing GraphQL queries and later interpreting the results
may be cumbersome. That's solved by our ``sgqlc.types``, which is
usually paired with ``sgqlc.operation`` to generate queries and then
interpret results (see more at ``examples/basic/02_schema_types.py``). The
example below matches a subset of 
`GitHub API v4 <https://developer.github.com/v4/query/>`_.
In GraphQL syntax it would be::

   query {
     repository(owner: "profusion", name: "sgqlc") {
       issues(first: 100) {
         nodes {
           number
           title
         }
         pageInfo {
           hasNextPage
           endCursor
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
         },
         "pageInfo": {
            "hasNextPage": false,
            "endCursor": "..."
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

   class IssueConnection(Connection):  # Connection provides page_info!
       nodes = list_of(Issue)

   class Repository(Type):
       issues = Field(IssueConnection, args=connection_args())

   class Query(Type):  # GraphQL's root
       repository = Field(Repository, args={'owner': str, 'name': str})

   # Generate an operation on Query, selecting fields:
   op = Operation(Query)
   # select a field, here with selection arguments, then another field:
   issues = op.repository(owner=owner, name=name).issues(first=100)
   # select sub-fields explicitly: { nodes { number title } }
   issues.nodes.number()
   issues.nodes.title()
   # here uses __fields__() to select by name (*args)
   issues.page_info.__fields__('has_next_page')
   # here uses __fields__() to select by name (**kwargs)
   issues.page_info.__fields__(end_cursor=True)

   # you can print the resulting GraphQL
   print(op)

   # Call the endpoint:
   data = endpoint(op)

   # Interpret results into native objects
   repo = (op + data).repository
   for issue in repo.issues.nodes:
       print(issue)


Why double-underscore and overloaded arithmetic methods?
========================================================

Since we don't want to clobber GraphQL fields, we cannot provide
nicely named methods. Therefore we use overloaded methods such as
``__iadd__``, ``__add__``, ``__bytes__`` (compressed GraphQL
representation) and ``__str__`` (indented GraphQL representation).

To select fields by name, use ``__fields__(*names, **names_and_args)``.
This helps with repetitive situations and can be used to "include all
fields", or "include all except...":

.. code-block:: python

  # just 'a' and 'b'
  type_selection.__fields__('a', 'b')
  type_selection.__fields__(a=True, b=True) # equivalent

  # a(arg1: value1), b(arg2: value2):
  type_selection.__fields__(
      a={'arg1': value1},
      b={'arg2': value2})

  # selects all possible fields
  type_selection.__fields__()

  # all but 'a' and 'b'
  type_selection.__fields__(__exclude__=('a', 'b'))
  type_selection.__fields__(a=False, b=False)


Code Generator
--------------

Manually converting an existing GraphQL schema to ``sgqlc.types``
subclasses is boring and error prone. To aid such task we offer a code
generator that outputs a Python module straight from JSON of an
introspection call:

.. code-block:: console

   user@host$ python3 -m sgqlc.introspection \
        --exclude-deprecated \
        --exclude-description \
        -H "Authorization: bearer ${GH_TOKEN}" \
        https://api.github.com/graphql \
        github_schema.json
   user@host$ sgqlc-codegen github_schema.json github_schema.py

This generates ``github_schema`` that provides the
:class:`sgqlc.types.Schema` instance of the same name ``github_schema``.
Then it's a matter of using that in your Python code, as in the example below
from ``examples/github/github-agile-dashboard.py``:

.. code-block:: python

   from sgqlc.operation import Operation
   from github_schema import github_schema as schema

   op = Operation(schema.Query)  # note 'schema.'

   # -- code below follows as the original usage example:

   # select a field, here with selection arguments, then another field:
   issues = op.repository(owner=owner, name=name).issues(first=100)
   # select sub-fields explicitly: { nodes { number title } }
   issues.nodes.number()
   issues.nodes.title()
   # here uses __fields__() to select by name (*args)
   issues.page_info.__fields__('has_next_page')
   # here uses __fields__() to select by name (**kwargs)
   issues.page_info.__fields__(end_cursor=True)

   # you can print the resulting GraphQL
   print(op)

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


Getting started developing
--------------------------

You need to use `pipenv <https://pipenv.readthedocs.io/en/latest>`_.

::

    pipenv install --dev
    pipenv shell

Install the git hooks:

::

   ./utils/git/install-git-hooks.sh

Run the tests (one of the below):

::

    ./utils/git/pre-commit       # flake8 and nose

    ./setup.py nosetests         # only nose (unit/doc tests)
    flake8 --config setup.cfg .  # style checks

Keep 100% coverage. You can look at the coverage report at
``cover/index.html``.  To do that, prefer 
`doctest <https://docs.python.org/3.7/library/doctest.html>`_
so it serves as
both documentation and test. However we use 
`nose <https://nose.readthedocs.io>`_ to write explicit tests that would be
hard to express using ``doctest``.

Build and review the generated Sphinx documentation, and validate if your
changes look right:

::

    ./setup.py build_sphinx
    open doc/build/html/index.html


To integrate changes from another branch, please **rebase** instead of
creating merge commits (
`read more <https://git-scm.com/book/en/v2/Git-Branching-Rebasing>`_).
