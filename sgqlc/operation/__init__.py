'''
Generate Operations (Query and Mutations) using Python
======================================================

.. note::

  This module could be called "query", however it should also generate
  mutations and a class ``Query`` could lead to mistakes, since the
  users should define their own root ``Query`` class with the
  top-level queries in their GraphQL schema.

Users create instance of :class:`Operation` using the
``Schema.Query`` or ``Schema.Mutation`` types. From there they proceed
accessing members, which will produce :class:`Selector` instances,
that once called will produce :class:`Selection` instances, which are
automatically added to a :class:`SelectionList` in the parent
(operation or selection). The following annotated GraphQL code helps
to understand the Python mapping::

   query { # Operation
      parent(arg: "value") { # Selector, called with arguments
         child { # Selector, called without arguments
            field # Selector called without arguments, Selection without alias
            alias: field(other: 123)
         }
         sibling { x { y } }
      }
   }

.. code-block:: python

   op = Operation(Query)
   parent = op.parent(arg='value')

   child = parent.child
   child.field()
   child.field(other=123, __alias__='alias')

   parent.sibling.x.y()

:class:`Operation` implements ``__str__()`` and ``__repr__()`` to
generate the GraphQL query for you. It also provide ``__bytes__()`` to
produce compact output, without indentation. It can be passed to
:class:`sgqlc.endpoint.base.BaseEndpoint.__call__()` as is.

Another convenience is the ``__add__()`` to apply the operation to a
resulting JSON data, interpreting the results and producing convenient
objects:

.. code-block:: python

   endpoint = HTTPEndpoint(url)
   data = endpoint(op)

   obj = op + data
   print(obj.parent.child.field)
   print(obj.parent.sibling.x.y)


Examples
--------

Let's start defining the types, including the schema root ``Query``:

>>> from sgqlc.types import *
>>> from datetime import datetime
>>> class Actor(Interface):
...    login = non_null(str)
...
>>> class User(Type, Actor):
...    name = str
...
>>> class Organization(Type, Actor):
...    location = str
...
>>> class ActorConnection(Type):
...    actors = Field(list_of(non_null(Actor)), args={'login': non_null(str)})
...
>>> class Assignee(Type):
...    email = non_null(str)
...
>>> class UserOrAssignee(Union):
...    __types__ = (User, Assignee)
...
>>> class Issue(Type):
...     number = non_null(int)
...     title = non_null(str)
...     body = str
...     reporter = non_null(User)
...     assigned = UserOrAssignee
...     commenters = ActorConnection
...
>>> class ReporterFilterInput(Input):
...     name_contains = str
...
>>> class IssuesFilter(Input):
...     reporter = list_of(ReporterFilterInput)
...     start_date = non_null(datetime)
...     end_date = datetime
...
>>> class Repository(Type):
...     id = ID
...     name = non_null(str)
...     owner = non_null(Actor)
...     issues = Field(list_of(non_null(Issue)), args={
...         'title_contains': str,
...         'reporter_login': str,
...         'filter': IssuesFilter,
...     })
...
>>> class Query(Type):
...     repository = Field(Repository, args={'id': non_null(ID)})
...
>>> class Mutation(Type):
...     add_issue = Field(Issue, args={
...         'repository_id': non_null(ID),
...         'title': non_null(str),
...         'body': str,
...     })
...
>>> global_schema  # doctest: +ELLIPSIS
schema {
  ...
  interface Actor {
    login: String!
  }
  type User implements Actor {
    login: String!
    name: String
  }
  type Organization implements Actor {
    login: String!
    location: String
  }
  type ActorConnection {
    actors(login: String!): [Actor!]
  }
  type Assignee {
    email: String!
  }
  union UserOrAssignee = User | Assignee
  type Issue {
    number: Int!
    title: String!
    body: String
    reporter: User!
    assigned: UserOrAssignee
    commenters: ActorConnection
  }
  input ReporterFilterInput {
    nameContains: String
  }
  input IssuesFilter {
    reporter: [ReporterFilterInput]
    startDate: DateTime!
    endDate: DateTime
  }
  type Repository {
    id: ID
    name: String!
    owner: Actor!
    issues(titleContains: String, reporterLogin: String, filter: IssuesFilter): [Issue!]
  }
  type Query {
    repository(id: ID!): Repository
  }
  type Mutation {
    addIssue(repositoryId: ID!, title: String!, body: String): Issue
  }
}

Selecting to Generate Queries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Then let's select numbers and titles of issues of repository with
identifier ``repo1``:

>>> op = Operation(Query)
>>> repository = op.repository(id='repo1')
>>> repository.issues.number()
number
>>> repository.issues.title()
title
>>> op # or repr(), prints out GraphQL!
query {
  repository(id: "repo1") {
    issues {
      number
      title
    }
  }
}

You can see we stored ``op.repository(id='repo1')`` result in a
variable, later reusing it. Executing this statement will emit a new
:class:`Selection` and only one field selection is allowed in the
selection list (unless an alias is used). Trying the code below will
**error**:

>>> op = Operation(Query)
>>> op.repository(id='repo1').issues.number() # ok!
number
>>> op.repository(id='repo1').issues.title() # fails
Traceback (most recent call last):
  ...
ValueError: repository already have a selection repository(id: "repo1") {
  issues {
    number
  }
}. Maybe use __alias__ as param?

That is, if you wanted to query for two repositories, you should use
``__alias__`` argument in the call. But here would **not** produce the
query we want, as seen below:

>>> op = Operation(Query)
>>> op.repository(id='repo1').issues.number()
number
>>> op.repository(id='repo1', __alias__='alias').issues.title()
title
>>> op  # not what we want in this example, 2 independent queries
query {
  repository(id: "repo1") {
    issues {
      number
    }
  }
  alias: repository(id: "repo1") {
    issues {
      title
    }
  }
}

In our case, to get the correct query, do as in the first example and
save the result of ``op.repository(id='repo1')``.

Aliases may be used to rename fields everywhere, not just in the topmost
query, and for other reasons other than allow two calls with the same
name. One may use it to translate API fields to something else, example:

>>> op = Operation(Query)
>>> repository = op.repository(id='repo1')
>>> repository.issues.number(__alias__='code')
code: number
>>> op # or repr(), prints out GraphQL!
query {
  repository(id: "repo1") {
    issues {
      code: number
    }
  }
}

Last but not least, in the first example you can also note that we're
not calling ``issues``, just accessing its members. This is a shortcut
for an empty call, and the handle is saved for you (ease of use):

>>> op = Operation(Query)
>>> repository = op.repository(id='repo1')
>>> repository.issues().number()
number
>>> repository.issues().title()
title
>>> op # or repr(), prints out GraphQL!
query {
  repository(id: "repo1") {
    issues {
      number
      title
    }
  }
}

This could be rewritten saving the issues selector:

>>> op = Operation(Query)
>>> issues = op.repository(id='repo1').issues()
>>> issues.number()
number
>>> issues.title()
title
>>> op
query {
  repository(id: "repo1") {
    issues {
      number
      title
    }
  }
}

Or even simpler with ``__fields__(*names, **names_and_args)``:

>>> op = Operation(Query)
>>> op.repository(id='repo1').issues.__fields__('number', 'title')
>>> op
query {
  repository(id: "repo1") {
    issues {
      number
      title
    }
  }
}
>>> op = Operation(Query)
>>> op.repository(id='repo1').issues.__fields__(
...     number=True,
...     title=True,
... )
>>> op
query {
  repository(id: "repo1") {
    issues {
      number
      title
    }
  }
}

Which also allows to include all but some fields:

>>> op = Operation(Query)
>>> op.repository(id='repo1').issues.__fields__(
...     __exclude__=('body', 'reporter', 'commenters'),
... )
>>> op
query {
  repository(id: "repo1") {
    issues {
      number
      title
      assigned {
        __typename
        ... on User {
          login
          name
        }
        ... on Assignee {
          email
        }
      }
    }
  }
}

Or using named arguments:

>>> op = Operation(Query)
>>> op.repository(id='repo1').issues.__fields__(
...     body=False,
...     reporter=False,
...     commenters=False,
... )
>>> op
query {
  repository(id: "repo1") {
    issues {
      number
      title
      assigned {
        __typename
        ... on User {
          login
          name
        }
        ... on Assignee {
          email
        }
      }
    }
  }
}

If no arguments are given to ``__fields__()``, then it defaults to
include every member, and this is done recursively:

>>> op = Operation(Query)
>>> op.repository(id='repo1').issues.__fields__()
>>> op
query {
  repository(id: "repo1") {
    issues {
      number
      title
      body
      reporter {
        login
        name
      }
      assigned {
        __typename
        ... on User {
          login
          name
        }
        ... on Assignee {
          email
        }
      }
      commenters {
        actors {
          login
        }
      }
    }
  }
}

Named arguments may be used to provide fields with argument values:

>>> op = Operation(Query)
>>> op.repository(id='repo1').__fields__(
...    issues={'title_contains': 'bug'}, # adds field and children
... )
>>> op
query {
  repository(id: "repo1") {
    issues(titleContains: "bug") {
      number
      title
      body
      reporter {
        login
        name
      }
      assigned {
        __typename
      }
    }
  }
}

Arguments can be given as tuple of key-value pairs as well:

>>> op = Operation(Query)
>>> op.repository(id='repo1').__fields__(
...    issues=(('title_contains', 'bug'),), # adds field and children
... )
>>> op
query {
  repository(id: "repo1") {
    issues(titleContains: "bug") {
      number
      title
      body
      reporter {
        login
        name
      }
      assigned {
        __typename
      }
    }
  }
}

If a field of a container type (interface or type) is used without explicit
fields as documented above, all of its fields will be added automatically.
It will avoid dependency loops and limit the allowed nest depth to 2 by
default, but that can be overridden with an explicit ``auto_select_depth``
to ``__to_graphql__()`` (which is used by ``str()``, ``repr()`` and the
likes):

>>> op = Operation(Query)
>>> op.repository(id='repo1') # printed with depth=2 (default)
repository(id: "repo1") {
  id
  name
  owner {
    login
  }
  issues {
    number
    title
    body
  }
}
>>> op # the whole query printed with depth=2 (default)
query {
  repository(id: "repo1") {
    id
    name
    owner {
      login
    }
    issues {
      number
      title
      body
    }
  }
}

>>> print(op.__to_graphql__(auto_select_depth=1)) # omits owner/issues
query {
  repository(id: "repo1") {
    id
    name
  }
}
>>> print(op.__to_graphql__(auto_select_depth=3)) # shows reporter
query {
  repository(id: "repo1") {
    id
    name
    owner {
      login
    }
    issues {
      number
      title
      body
      reporter {
        login
        name
      }
      assigned {
        __typename
      }
    }
  }
}
>>> print(op.__to_graphql__(auto_select_depth=4)) # shows assigned sub-types
query {
  repository(id: "repo1") {
    id
    name
    owner {
      login
    }
    issues {
      number
      title
      body
      reporter {
        login
        name
      }
      assigned {
        __typename
        ... on User {
          login
          name
        }
        ... on Assignee {
          email
        }
      }
      commenters {
        actors {
          login
        }
      }
    }
  }
}





Interpret Query Results
~~~~~~~~~~~~~~~~~~~~~~~

Given the operation explained above:

>>> op = Operation(Query)
>>> op.repository(id='repo1').issues.__fields__('number', 'title')
>>> op
query {
  repository(id: "repo1") {
    issues {
      number
      title
    }
  }
}

After calling the GraphQL endpoint, you should get a JSON object that
matches the one below:

>>> json_data = {'data': {
...     'repository': {'issues': [
...         {'number': 1, 'title': 'found a bug'},
...         {'number': 2, 'title': 'a feature request'},
...     ]},
... }}

To interpret this, simply add the data to the operation:

>>> obj = op + json_data
>>> repository = obj.repository
>>> for issue in repository.issues:
...     print(issue)
Issue(number=1, title=found a bug)
Issue(number=2, title=a feature request)

Which are instances of classes declared in the beginning of example
section:

>>> repository.__class__ is Repository
True
>>> repository.issues[0].__class__ is Issue
True

While it's mostly the same as creating instances yourself:

>>> repository = Repository(json_data['data']['repository'])
>>> for issue in repository.issues:
...     print(issue)
Issue(number=1, title=found a bug)
Issue(number=2, title=a feature request)

The difference is that it will handle **aliases** for you:

>>> op = Operation(Query)
>>> op.repository(id='repo1', __alias__='r_name1').issues.__fields__(
...     number='code', title='headline',
... )
>>> op.repository(id='repo2', __alias__='r_name2').issues.__fields__(
...     'number', 'title',
... )
>>> op
query {
  r_name1: repository(id: "repo1") {
    issues {
      code: number
      headline: title
    }
  }
  r_name2: repository(id: "repo2") {
    issues {
      number
      title
    }
  }
}

>>> json_data = {'data': {
...     'r_name1': {'issues': [
...         {'code': 1, 'headline': 'found a bug'},
...         {'code': 2, 'headline': 'a feature request'},
...     ]},
...     'r_name2': {'issues': [
...         {'number': 10, 'title': 'something awesome'},
...         {'number': 20, 'title': 'other thing broken'},
...     ]},
... }}
>>> obj = op + json_data
>>> for issue in obj.r_name1.issues:
...     print(issue)
Issue(code=1, headline=found a bug)
Issue(code=2, headline=a feature request)
>>> for issue in obj.r_name2.issues:
...     print(issue)
Issue(number=10, title=something awesome)
Issue(number=20, title=other thing broken)

Updating also reflects on the correct backing store:

>>> obj.r_name2.name = 'repo2 name'
>>> json_data['data']['r_name2']['name']
'repo2 name'

It also works with auto selection:

>>> op = Operation(Query)
>>> op.repository(id='repo1')
repository(id: "repo1") {
  id
  name
  owner {
    login
  }
  issues {
    number
    title
    body
  }
}
>>> json_data = {'data': {
...     'repository': {'id': 'repo1', 'name': 'Repo #1'},
... }}
>>> obj = op + json_data
>>> obj.repository.name
'Repo #1'


Error Reporting
~~~~~~~~~~~~~~~

If the returned data contains only ``errors`` and no ``data``,
the interpretation will raise an error :class:`GraphQLErrors`:

>>> json_data = {'errors': [{'message': 'some message'}]}
>>> try:  # doctest: +ELLIPSIS
...     obj = op + json_data
... except GraphQLErrors as ex:
...     print('Got error:', repr(ex))
...     print(ex.errors)
Got error: GraphQLErrors('some message'...
[{'message': 'some message'}]

If there are mixed data and errors, the object is returned with
``__errors__`` attribute set to the errors:

>>> json_data = {
...     'errors': [{'message': 'some message'}],
...     'data': {
...         'repository': {'id': 'repo1', 'name': 'Repo #1'},
...     },
... }
>>> obj = op + json_data
>>> obj.repository.name
'Repo #1'
>>> obj.__errors__
[{'message': 'some message'}]


Mutations
~~~~~~~~~

Mutations are handled as well, just use that as :class:`Operation`
root type:

>>> op = Operation(Mutation)
>>> op.add_issue(repository_id='repo1', title='an issue').__fields__()
>>> op
mutation {
  addIssue(repositoryId: "repo1", title: "an issue") {
    number
    title
    body
    reporter {
      login
      name
    }
    assigned {
      __typename
      ... on User {
        login
        name
      }
      ... on Assignee {
        email
      }
    }
    commenters {
      actors {
        login
      }
    }
  }
}


Inline Fragments & Interfaces
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When a field specifies an interface such as the ``Repository.owner``
in our example, only the interface fields can be queried. However,
the actual type may implement much more, and to solve that in GraphQL
we usually do an inline fragment ``... on ActualType { field1, field2 }``.

To achieve that we use the ``__as__(ActualType)`` on the selection list,
example:

>>> op = Operation(Query)
>>> repo = op.repository(id='repo1')
>>> repo.owner.login() # interface fields can be declared as usual
login
>>> repo.owner().__as__(Organization).location() # location field for Orgs
location
>>> repo.owner.__as__(User).name() # name field for Users
name
>>> repo.issues().assigned.__as__(Assignee).email()
email
>>> repo.issues().assigned.__as__(User).login()
login
>>> repo.issues().commenters().actors().login()
login
>>> repo.issues().commenters().actors().__as__(Organization).location()
location
>>> repo.issues().commenters().actors().__as__(User).name()
name
>>> op
query {
  repository(id: "repo1") {
    owner {
      login
      __typename
      ... on Organization {
        location
      }
      ... on User {
        name
      }
    }
    issues {
      assigned {
        __typename
        ... on Assignee {
          email
        }
        ... on User {
          login
        }
      }
      commenters {
        actors {
          login
          __typename
          ... on Organization {
            location
          }
          ... on User {
            name
          }
        }
      }
    }
  }
}

Note that ``__typename`` is automatically selected so it can create the
proper type when interprets the results:

>>> json_data = {'data': {'repository': {'owner': {
...    '__typename': 'User',
...    'login': 'user',
...    'name': 'User Name',
...    },
...    'issues': [
...      {
...          'assigned': {'__typename': 'Assignee', 'email': 'e@mail.com'},
...          'commenters': {
...              'actors': [
...                  {'login': 'user', '__typename': 'User', 'name': 'User Name'},
...                  {'login': 'a-company', '__typename': 'Organization', 'location': 'that place'}
...              ]
...          }
...      },
...      {
...          'assigned': {'__typename': 'User', 'login': 'xpto'},
...          'commenters': {
...              'actors': [
...                  {'login': 'user', '__typename': 'User', 'name': 'User Name'},
...                  {'login': 'xpto', '__typename': 'User'}
...              ]
...          }
...      },
...    ],
... }}}
>>> obj = op + json_data
>>> obj.repository.owner
User(login='user', __typename__='User', name='User Name')
>>> for i in obj.repository.issues:
...     print(i)
Issue(assigned=Assignee(__typename__=Assignee, email=e@mail.com), commenters=ActorConnection(actors=[User(login='user', __typename__='User', name='User Name'), Organization(login='a-company', __typename__='Organization', location='that place')]))
Issue(assigned=User(__typename__=User, login=xpto), commenters=ActorConnection(actors=[User(login='user', __typename__='User', name='User Name'), User(login='xpto', __typename__='User')]))

>>> json_data = {'data': {'repository': {'owner': {
...    '__typename': 'Organization',
...    'login': 'a-company',
...    'name': 'A Company',
... }}}}
>>> obj = op + json_data
>>> obj.repository.owner
Organization(login='a-company', __typename__='Organization')

If the returned type doesn't have an explicit type fields, the
Interface field is returned:

>>> json_data = {'data': {'repository': {'owner': {
...    '__typename': 'SomethingElse',
...    'login': 'something-else',
...    'field': 'value',
... }}}}
>>> obj = op + json_data
>>> obj.repository.owner
Actor(login='something-else', __typename__='SomethingElse')

In the unusual situation where ``__typename`` is not returned,
it's going to behave as the interface type as well:

>>> json_data = {'data': {'repository': {'owner': {
...    'login': 'user',
...    'name': 'User Name',
... }}}}
>>> obj = op + json_data
>>> obj.repository.owner
Actor(login='user')


Named Fragments
~~~~~~~~~~~~~~~

Named fragments are a way to reuse selection blocks and allow
optimizations to be employed. They also allow shorter documents
if the fragment is used more than once.

They are similar to Inline Fragments described above as they
allow selecting on interfaces and unions.

>>> org_loc_frag = Fragment(Organization, 'OrganizationLocationFragment')
>>> org_loc_frag.location()
location
>>> org_login_frag = Fragment(Organization, 'OrganizationLoginFragment')
>>> org_login_frag.login()
login
>>> user_frag = Fragment(User, 'UserFragment')
>>> user_frag.name()
name
>>> assignee_frag = Fragment(Assignee, 'AssigneeFragment')
>>> assignee_frag.email()
email
>>> op = Operation(Query)
>>> repo = op.repository(id='repo1')
>>> repo.owner.login() # interface fields can be declared as usual
login
>>> repo.owner().__fragment__(org_loc_frag)
>>> repo.owner().__fragment__(org_login_frag)  # can do many on the same type
>>> repo.owner.__fragment__(user_frag)
>>> repo.issues().assigned.__fragment__(assignee_frag)
>>> repo.issues().assigned.__fragment__(user_frag)
>>> repo.issues().commenters().actors().login()
login
>>> repo.issues().commenters().actors().__fragment__(org_loc_frag)
>>> repo.issues().commenters().actors().__fragment__(user_frag)
>>> op
query {
  repository(id: "repo1") {
    owner {
      login
      __typename
      ...OrganizationLocationFragment
      ...OrganizationLoginFragment
      ...UserFragment
    }
    issues {
      assigned {
        __typename
        ...AssigneeFragment
        ...UserFragment
      }
      commenters {
        actors {
          login
          __typename
          ...OrganizationLocationFragment
          ...UserFragment
        }
      }
    }
  }
}
fragment OrganizationLocationFragment on Organization {
  location
}
fragment OrganizationLoginFragment on Organization {
  login
}
fragment UserFragment on User {
  name
}
fragment AssigneeFragment on Assignee {
  email
}

Note that ``__typename`` is automatically selected so it can create the
proper type when interprets the results:

>>> json_data = {'data': {'repository': {'owner': {
...    '__typename': 'User',
...    'login': 'user',
...    'name': 'User Name',
...    },
...    'issues': [
...      {
...          'assigned': {'__typename': 'Assignee', 'email': 'e@mail.com'},
...          'commenters': {
...              'actors': [
...                  {'login': 'user', '__typename': 'User', 'name': 'User Name'},
...                  {'login': 'a-company', '__typename': 'Organization', 'location': 'that place'}
...              ]
...          }
...      },
...      {
...          'assigned': {'__typename': 'User', 'name': 'User'},
...          'commenters': {
...              'actors': [
...                  {'login': 'user', '__typename': 'User', 'name': 'User Name'},
...                  {'login': 'xpto', '__typename': 'User'}
...              ]
...          }
...      },
...    ],
... }}}
>>> obj = op + json_data
>>> obj.repository.owner
User(login='user', __typename__='User', name='User Name')
>>> for i in obj.repository.issues:
...     print(i)
Issue(assigned=Assignee(__typename__=Assignee, email=e@mail.com), commenters=ActorConnection(actors=[User(login='user', __typename__='User', name='User Name'), Organization(login='a-company', __typename__='Organization', location='that place')]))
Issue(assigned=User(__typename__=User, name=User), commenters=ActorConnection(actors=[User(login='user', __typename__='User', name='User Name'), User(login='xpto', __typename__='User')]))

>>> json_data = {'data': {'repository': {'owner': {
...    '__typename': 'Organization',
...    'login': 'a-company',
...    'location': 'somewhere',
...    'name': 'A Company',
... }}}}
>>> obj = op + json_data
>>> obj.repository.owner
Organization(login='a-company', __typename__='Organization', location='somewhere')

If the returned type doesn't have an explicit type fields, the
Interface field is returned:

>>> json_data = {'data': {'repository': {'owner': {
...    '__typename': 'SomethingElse',
...    'login': 'something-else',
...    'field': 'value',
... }}}}
>>> obj = op + json_data
>>> obj.repository.owner
Actor(login='something-else', __typename__='SomethingElse')

In the unusual situation where ``__typename`` is not returned,
it's going to behave as the interface type as well:

>>> json_data = {'data': {'repository': {'owner': {
...    'login': 'user',
...    'name': 'User Name',
... }}}}
>>> obj = op + json_data
>>> obj.repository.owner
Actor(login='user')


Utilities
~~~~~~~~~

Starting with the first selection example:

>>> op = Operation(Query)
>>> repository = op.repository(id='repo1')
>>> repository.issues.number()
number
>>> repository.issues.title()
title

One can get a indented print out using ``repr()``:

>>> print(repr(op))
query {
  repository(id: "repo1") {
    issues {
      number
      title
    }
  }
}
>>> print(repr(repository))
repository(id: "repo1") {
  issues {
    number
    title
  }
}
>>> print(repr(repository.issues.number()))
number

Note that :class:`Selector` is different:

>>> print(repr(repository.issues.number))
Selector(field=number)

Or can get a compact print out without indentation using ``bytes()``:

>>> print(bytes(op).decode('utf-8'))
query {
repository(id: "repo1") {
issues {
number
title
}
}
}
>>> print(bytes(repository).decode('utf-8'))
repository(id: "repo1") {
issues {
number
title
}
}
>>> print(bytes(repository.issues.number()).decode('utf-8'))
number


:class:`Selection` and :class:`Selector` both implement ``len()``:

>>> len(op)                        # number of selections (here: top level)
1
>>> len(repository.issues())       # number of selections
2
>>> len(repository.issues)         # number of selections (implicit empty call)
2
>>> len(repository.issues.title()) # leaf is always 1
1

:class:`Selection` and :class:`Selector` both implement ``dir()`` to
also list fields:

>>> for name in dir(repository.issues()): # on selection also yields fields
...     if not name.startswith('_'):
...         print(name)
assigned
body
commenters
number
reporter
title
>>> for name in dir(repository.issues): # same for selector
...     if not name.startswith('_'):
...         print(name)
assigned
body
commenters
number
reporter
title
>>> for name in dir(repository.issues.number()): # no fields for scalar
...     if not name.startswith('_'):
...         print(name)
>>> for name in dir(repository.issues.number): # no fields for scalar
...     if not name.startswith('_'):
...         print(name)

Classes also implement ``iter()`` to iterate over selections:

>>> for i, sel in enumerate(op):
...     print('#%d: %s' % (i, sel))
#0: repository(id: "repo1") {
  issues {
    number
    title
  }
}
>>> for i, sel in enumerate(repository):
...     print('#%d: %s' % (i, sel))
#0: issues {
  number
  title
}
>>> for i, sel in enumerate(repository.issues):
...     print('#%d: %s' % (i, sel))
#0: number
#1: title
>>> for i, sel in enumerate(repository.issues()):
...     print('#%d: %s' % (i, sel))
#0: number
#1: title
>>> for i, sel in enumerate(repository.issues.number()):
...     print('#%d: %s' % (i, sel))
#0: number

Given a :class:`Selector` one can query a **selection** given its alias:

>>> op = Operation(Query)
>>> op.repository(id='repo1').issues.number()
number
>>> op.repository(id='repo2', __alias__='alias').issues.title()
title
>>> type(op['repository'])  # it's the selector, not a selection!
<class 'sgqlc.operation.Selector'>
>>> op['repository'].__selection__() # default selection
repository(id: "repo1") {
  issues {
    number
  }
}
>>> op['repository'].__selection__('alias') # aliased selection
alias: repository(id: "repo2") {
  issues {
    title
  }
}

Which is useful to query the selection alias and arguments:

>>> op['repository'].__selection__('alias').__alias__
'alias'
>>> op['repository'].__selection__('alias').__args__
{'id': 'repo2'}
>>> op['repository'].__selection__().__args__
{'id': 'repo1'}

To get the arguments of the default (non-aliased) one can use the shortcut:

>>> op['repository'].__args__
{'id': 'repo1'}

:license: ISC
'''  # noqa: E501

__docformat__ = 'reStructuredText en'

__all__ = ('Operation',)

from collections import OrderedDict

from ..types import BaseTypeWithTypename, Union, ContainerType, ArgDict, \
    global_schema


DEFAULT_AUTO_SELECT_DEPTH = 2
PROXIED_FIELDS = {
    '__type__', '__casts__', '__as__', '__fragment__', '__fragments__',
}


class Selection:
    '''Select a field with in a container type.

    .. warning::

      Do not create instances directly, use
      :class:`sgqlc.operation.Selector` instead.

    A selection matches the GraphQL statement to select a field from a
    type, it may contain an alias and parameters::

      query {
        parent {
          field
          field(param1: value1, param2: value2)
          alias: field(param1: value1, param2: value2)
        }
      }

    Attributes or items access will result in :class:`sgqlc.operation.Selector`
    matching the **target type** field:

    .. code-block:: python

      parent.field.child


    For container types one can provide a batch of fields using
    :func:`sgqlc.operation.Selection.__fields__()`:

    .. code-block:: python

      # just field1 and field2
      parent.field.child.__fields__('field1', 'field2')
      parent.field.child.__fields__(field1=True, field2=True)

      # field1 with parameters
      parent.field.child.__fields__(field1=dict(param1='value1'))

      # all but field2
      parent.field.child.__fields__(field2=False)
      parent.field.child.__fields__(field2=None)
      parent.field.child.__fields__(__exclude__=('field2',))

    If ``__fields__()`` is not explicitly called, then all fields
    are included. Note that this may lead to huge queries since it
    will result in recursive inclusion of all fields.

    Selectors will create selections when items or attributes are
    accessed, this is done by implicitly calling the selector with
    empty parameters.

    However leafs (ie: scalars) must be **explicitly** called,
    otherwise they won't generate a selection

    .. code-block:: python

      # OK
      parent.field.child()
      # NOT OK: doesn't create a selection for child.
      parent.field.child

    '''

    __slots__ = (
        '__alias__', '__field__', '__args__', '__field_selector',
        '__selection_list',
    )

    def __init__(self, alias, field, args):
        self.__alias__ = alias
        self.__field__ = field
        self.__args__ = args
        self.__field_selector = {}
        self.__selection_list = None
        if issubclass(field.type, BaseTypeWithTypename):
            self.__selection_list = SelectionList(field.type)

    def __get_selections_or_auto_select__(
            self, auto_select_depth=DEFAULT_AUTO_SELECT_DEPTH):
        selections = self.__selection_list
        if selections is None or selections:
            return selections
        return self.__get_all_fields_selection_list(
            auto_select_depth, [])

    def __len__(self):
        if self.__selection_list is not None:
            return len(self.__selection_list)
        return 1

    def __iter__(self):
        if self.__selection_list is not None:
            return iter(self.__selection_list)
        return iter((self,))

    def __select_all_types(cls, union_type, depth, trail):
        recursive = len(trail) < depth

        q = SelectionList(union_type)
        q.__typename__()
        for t in union_type:
            if recursive and t not in trail:
                sel = q.__as__(t)
                for x in cls.__select_all_fields(t, depth, trail):
                    sel += x
        return q

    def __select_all_fields(cls, container_type, depth, trail):
        recursive = len(trail) < depth

        q = SelectionList(container_type)
        for f in container_type:
            sel = Selection(None, f, {})
            if issubclass(f.type, BaseTypeWithTypename):
                if recursive and f.type not in trail:
                    # change the locally created selection list to the
                    # auto-selected one. This must be explicit here so
                    # it doesn't affect __to_graphql__(), that one must not
                    # affect the actual selection it's operating on!
                    sel.__selection_list = \
                        sel.__get_all_fields_selection_list(depth, trail)
                else:
                    sel = None

            if sel:
                q += sel
        return q

    def __get_all_fields_selection_list(self, depth, trail):
        t = self.__field__.type
        trail.append(t)

        if issubclass(t, Union):
            q = self.__select_all_types(t, depth, trail)
        else:
            q = self.__select_all_fields(t, depth, trail)

        trail.pop()
        return q

    def __fields__(self, *names, **names_and_args):
        '''Select fields of a container type.

        This is a helper to automate selection of fields of container
        types, such as giving a list of names to include, with or
        without parameters (passed as a mapping ``name=args``).

        If no arguments are given, all fields are included.

        If the keyword argument ``__exclude__`` is given a list of
        names, then all but those fields will be
        included. Alternatively one can exclude fields using
        ``name=None`` or ``name=False`` as keyword argument.

        If a list of names is given as positional arguments, then only
        those names will be included. Alternatively one can include
        fields using ``name=True``. To include fields with selection
        parameters, then use ``name=dict(...)`` or ``name=list(...)``.
        To include fields without arguments and with aliases, use the
        shortcut ``name='alias'``.

        .. code-block:: python

          # just field1 and field2
          parent.field.child.__fields__('field1', 'field2')
          parent.field.child.__fields__(field1=True, field2=True)

          # field1 with parameters
          parent.field.child.__fields__(field1=dict(param1='value1'))

          # field1 renamed (aliased) to alias1
          parent.field.child.__fields__(field1='alias1')

          # all but field2
          parent.field.child.__fields__(field2=False)
          parent.field.child.__fields__(field2=None)
          parent.field.child.__fields__(__exclude__=('field2',))
        '''
        exclude = self.__fields_gen_excludes(names_and_args)

        if not names and not names_and_args:
            self.__fields_add_all(exclude)
            return

        self.__fields_add_names(names)
        self.__fields_add_names_and_args(names_and_args)

    def __fields_gen_excludes(self, names_and_args):
        exclude = []
        if '__exclude__' in names_and_args:
            exclude = names_and_args.pop('__exclude__')

        for k, v in tuple(names_and_args.items()):  # force copy
            if v is False or v is None:
                exclude.append(k)
                del names_and_args[k]

        return exclude

    def __fields_add_all(self, exclude):
        for f in self.__field__.type:
            if f.name not in exclude:
                self[f.name]()

    def __fields_add_names(self, names):
        for n in names:
            self[n]()

    def __fields_add_names_and_args(self, names_and_args):
        for n, args in names_and_args.items():
            if args and not isinstance(args, dict):
                if isinstance(args, (tuple, list)):
                    args = dict(args)
                elif isinstance(args, str):
                    args = {'__alias__': args}
                else:
                    args = {}
            self[n](**args)

    def __to_graphql__(self, indent=0, indent_string='  ',
                       auto_select_depth=DEFAULT_AUTO_SELECT_DEPTH):
        prefix = indent_string * indent

        alias = ''
        if self.__alias__:
            alias = self.__alias__ + ': '

        args = self.__field__.args.__to_graphql_input__(
            self.__args__, indent, indent_string)

        query = ''
        if self.__selection_list is not None:
            selections = self.__selection_list
            if not selections:
                selections = self.__get_all_fields_selection_list(
                    auto_select_depth, [])
            query = ' ' + selections.__to_graphql__(
                indent, indent_string, auto_select_depth)
        return prefix + alias + self.__field__.graphql_name + args + query

    def __collect_fragments__(self, fragments):
        if self.__selection_list:
            self.__selection_list.__collect_fragments__(fragments)

    def __dir__(self):
        original_dir = super(Selection, self).__dir__()
        t = self.__field__.type
        if not issubclass(t, ContainerType):
            return original_dir
        fields = [f.name for f in t]
        return sorted(original_dir + fields)

    def __getattr__(self, name):
        if name.startswith('_'):
            sl = self.__selection_list
            if name in PROXIED_FIELDS:
                if sl is None:
                    return None
                return getattr(sl, name)

        try:
            return self[name]
        except KeyError as exc:
            raise AttributeError('%s has no field %s' % (self, name)) from exc
        except ValueError as exc:
            raise AttributeError('%s failed to get field %s' %
                                 (self, name)) from exc

    def __getitem__(self, name):
        if self.__selection_list is None:
            raise ValueError('Field %r of %s is not a container type.' %
                             (self.__field__, self.__field__.container))

        selector = self.__field_selector.get(name)
        if selector is None:
            selector = self.__field_selector[name] = Selector(
                self.__selection_list, self.__field__.type[name])

        return selector

    def __str__(self):
        return self.__to_graphql__()

    def __repr__(self):
        return str(self)

    def __bytes__(self):
        return bytes(self.__to_graphql__(indent_string=''), 'utf-8')


class Selector:
    '''Creates selection for a given field.

    .. warning::

      Do not create instances directly, use
      :class:`sgqlc.operation.SelectionList` instead.

    Selectors are callable objects that will create
    :class:`sgqlc.operation.Selection` entries in the parent
    :class:`sgqlc.operation.SelectionList`.

    Selectors will create selections when items or attributes are
    accessed, this is done by implicitly calling the selector with
    empty parameters.

    However leafs (ie: scalars) must be **explicitly** called,
    otherwise they won't generate a selection

    .. code-block:: python

      # OK
      parent.field.child()
      # NOT OK: doesn't create a selection for child.
      parent.field.child

    To select all fields from a container type, use
    :func:`sgqlc.operation.Selection.__fields__()`, example:

    .. code-block:: python

      # just field1 and field2
      parent.field.child.__fields__('field1', 'field2')
      parent.field.child.__fields__(field1=True, field2=True)

      # field1 with parameters
      parent.field.child.__fields__(field1=dict(param1='value1'))

      # all but field2
      parent.field.child.__fields__(field2=False)
      parent.field.child.__fields__(field2=None)
      parent.field.child.__fields__(__exclude__=('field2',))

    .. note::

       GraphQL limits a single selection per type, as the field name
       is used in the return object. If you want to select the same
       field multiple times, like as using different parameters, then
       provide the ``__alias__`` parameter to the selector:

        .. code-block:: python

          # FAILS:
          parent.field.child(param1='value1')
          parent.field.child(param2='value2')

          # OK
          parent.field.child(param1='value1')
          parent.field.child(param2='value2', __alias__='child2')
    '''

    __slots__ = (
        '__parent__', '__field__', '__selections',
    )

    def __init__(self, parent, field):
        self.__parent__ = parent
        self.__field__ = field
        self.__selections = {}

    def __call__(self, **args):
        '''Create a selection with the given parameters.

        To provide an alias, use ``__alias__`` keyword argument.
        '''
        alias = None
        if '__alias__' in args:
            alias = args.pop('__alias__')

        s = self.__selections.get(alias)
        if s is not None:
            if not args:
                return s
            raise ValueError(
                ('%s already have a selection %s. '
                 'Maybe use __alias__ as param?') % (self.__field__, s))

        s = self.__selections[alias] = Selection(alias, self.__field__, args)
        self.__parent__ += s
        return s

    def __as__(self, typ):
        '''Create a selection list on the given type.

        The selection list will be result in an inline fragment
        in the query with an additional query for ``__typename``,
        which is later used to create the proper type when
        the results are interpreted.
        '''
        return self().__as__(typ)

    def __fragment__(self, fragment):
        '''Spread the given fragment in the selection list.
        '''
        return self().__fragment__(fragment)

    def __dir__(self):
        original_dir = super(Selector, self).__dir__()
        t = self.__field__.type
        if not issubclass(t, ContainerType):
            return original_dir
        fields = [f.name for f in t]
        return sorted(original_dir + fields)

    @property
    def __fields__(self):
        '''Calls the selector without arguments, creating a
        :class:`Selection` instance and return
        :func:`Selection.__fields__` method, ready to be called.

        To query the actual field this selector operates, use
        ``self.__field__``
        '''
        return self().__fields__

    def __len__(self):
        return len(self())

    def __iter__(self):
        return iter(self())

    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError as exc:
            raise AttributeError('%s has no field %s' % (self, name)) from exc
        except ValueError as exc:
            raise AttributeError('%s failed to get field %s' %
                                 (self, name)) from exc

    def __getitem__(self, name):
        return self()[name]

    def __str__(self):
        return '%s(field=%s)' % (self.__class__.__name__, self.__field__)

    def __repr__(self):
        return str(self)

    def __selection__(self, alias=None):
        'Return the selection given its alias'
        return self.__selections[alias]

    @property
    def __args__(self):
        'Shortcut for self.__selection__().__args__'
        return self.__selection__().__args__


class SelectionList:
    '''List of :class:`sgqlc.operation.Selection` in a type.

    .. warning::

      Do not create instances directly, use
      :class:`sgqlc.operation.Operation` instead.

    Create a selection list using a type to query its fields. Once
    fields are accessed, they will create
    :class:`sgqlc.operation.Selector` object for that field, this
    allows to match the type structure, with easy to use API:

    .. code-block:: python

      parent.field.child()
      parent.field(param1=value1).child()

    Direct usage example (not recommended):

    >>> sl = SelectionList(global_schema.Repository)
    >>> sl += Selection('x', global_schema.Repository.id, {})
    >>> sl # or repr()
    {
      x: id
    }
    >>> print(bytes(sl).decode('utf-8')) # no indentation
    {
    x: id
    }
    >>> sl.id    # or any other field from Repository returns a Selector
    Selector(field=id)
    >>> sl['id'] # also as get item
    Selector(field=id)
    >>> sl.x    # not the alias
    Traceback (most recent call last):
      ...
    AttributeError: {
      x: id
    } has no field x
    >>> sl['x'] #
    Traceback (most recent call last):
      ...
    KeyError: 'Repository has no field x'
    >>> sl.__type__ # returns the type the selection operates on
    type Repository {
      id: ID
      name: String!
      owner: Actor!
      issues(titleContains: String, reporterLogin: String, filter: IssuesFilter): [Issue!]
    }

    '''  # noqa: E501

    __slots__ = ('__type', '__selectors', '__selections', '__casts',
                 '__fragments')

    def __init__(self, typ):
        assert issubclass(typ, BaseTypeWithTypename), \
            str(typ) + ': not a selection list type (container or union)'
        self.__type = typ
        self.__selectors = {}
        self.__selections = []
        self.__casts = OrderedDict()
        self.__fragments = OrderedDict()

    def __str__(self):
        return self.__to_graphql__()

    def __repr__(self):
        return str(self)

    def __bytes__(self):
        return bytes(self.__to_graphql__(indent_string=''), 'utf-8')

    def __to_graphql__(self, indent=0, indent_string='  ',
                       auto_select_depth=DEFAULT_AUTO_SELECT_DEPTH):
        prefix = indent_string * indent
        next_indent = indent + 1

        s = ['{']
        for v in self.__selections:
            s.append(v.__to_graphql__(
                next_indent, indent_string, auto_select_depth,
            ))

        next_prefix = prefix + indent_string
        for v in self.__casts.values():
            s.append(next_prefix + v.__to_graphql__(
                next_indent, indent_string, auto_select_depth,
            ))
        for lst in self.__fragments.values():
            for v in lst:
                s.append(next_prefix + v.__spread__())

        s.append(prefix + '}')
        return '\n'.join(s)

    def __get_selections_or_auto_select__(self):
        return self.__selections

    def __iter__(self):
        return iter(self.__selections)

    def __len__(self):
        return len(self.__selections)

    def __getitem__(self, name):
        s = self.__selectors.get(name)
        if s is None:
            s = self.__selectors[name] = Selector(self, self.__type[name])
        return s

    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError as exc:
            raise AttributeError('%s has no field %s' % (self, name)) from exc

    def __iadd__(self, selection):
        assert isinstance(selection, Selection)
        self.__selections.append(selection)
        return self

    @property
    def __type__(self):
        return self.__type

    @property
    def __casts__(self):
        return self.__casts

    @property
    def __fragments__(self):
        return self.__fragments

    def __collect_fragments__(self, fragments=None):
        if fragments is None:
            fragments = OrderedDict()

        for lst in self.__fragments.values():
            for frag in lst:
                fragments.setdefault(frag.__name__, frag)
                frag.__collect_fragments__(fragments)

        for sel in self.__selections:
            sel.__collect_fragments__(fragments)

        return fragments

    def __as__(self, typ):
        '''Create a child selection list on the given type.

        The selection list will be result in an inline fragment
        in the query with an additional query for ``__typename``,
        which is later used to create the proper type when
        the results are interpreted.

        The newly created selection list is shared for all users
        of the same type in this selection list.
        '''
        try:
            return self.__casts[typ.__name__]
        except KeyError:
            pass

        sl = InlineFragmentSelectionList(typ)
        self.__casts[typ.__name__] = sl
        self['__typename__']()
        return sl

    def __fragment__(self, fragment):
        assert isinstance(fragment, Fragment)
        self.__fragments.setdefault(
            fragment.__type__.__name__, []
        ).append(fragment)
        self['__typename__']()


class InlineFragmentSelectionList(SelectionList):
    def __to_graphql__(self, indent=0, indent_string='  ',
                       auto_select_depth=DEFAULT_AUTO_SELECT_DEPTH):
        selection = SelectionList.__to_graphql__(
            self, indent, indent_string, auto_select_depth)
        return '... on %s %s' % (self.__type__, selection)


class Fragment(SelectionList):
    __slots__ = ('__name',)

    def __init__(self, typ, name):
        super(Fragment, self).__init__(typ)
        self.__name = name

    @property
    def __name__(self):
        return self.__name

    def __spread__(self):
        return '...%s' % (self.__name,)

    def __to_graphql__(self, indent=0, indent_string='  ',
                       auto_select_depth=DEFAULT_AUTO_SELECT_DEPTH):
        selection = SelectionList.__to_graphql__(
            self, indent, indent_string, auto_select_depth)
        return 'fragment %s on %s %s' % (
            self.__name, self.__type__, selection)


class GraphQLErrors(RuntimeError):
    def __init__(self, errors):
        assert len(errors) > 0
        msg = str(errors[0].get('message'))
        super(RuntimeError, self).__init__(msg)
        self.errors = errors


class Operation:
    '''GraphQL Operation: query or mutation.

    The given type must be one of ``schema.Query`` or
    ``schema.Mutation``, defaults to ``global_schema.Query`` or
    whatever is defined as ``global_schema.query_type``.

    The operation has an internal
    :class:`sgqlc.operation.SelectionList` and will proxy attributes
    and item access to it, thus offering selectors and automatically
    handling selections:

    .. code-block:: python

      op = Operation()
      op.parent.field.child()
      op.parent.field(param1=value1, __alias__'q2').child()

    Once data is fetched and parsed as JSON object containing the
    field ``data``, the operation can be used to interpret this data
    using the addition operator (no clearly named method to avoid
    clashing with selections):

    .. code-block:: python

      op = Operation()
      op.parent.field.child()

      endpoint = HTTPEndpoint('http://my.server.com/graphql')
      json_data = endpoint(op)

      parent = op + json_data
      print(parent.field.child)

    Example usage:

    >>> op = Operation(global_schema.Query)
    >>> op.repository
    Selector(field=repository)
    >>> repository = op.repository(id='repo1')
    >>> repository.issues.number()
    number
    >>> repository.issues.title()
    title
    >>> op # or repr(), prints out GraphQL!
    query {
      repository(id: "repo1") {
        issues {
          number
          title
        }
      }
    }

    The root type can be omitted, then ``global_schema.Query`` or
    whatever is defined as ```global_schema.query_type`` is used:

    >>> op = Operation()  # same as Operation(global_schema.Query)
    >>> op.repository
    Selector(field=repository)

    Operations can be named:

    >>> op = Operation(name='MyOp')
    >>> repository = op.repository(id='repo1')
    >>> repository.issues.number()
    number
    >>> repository.issues.title()
    title
    >>> op # or repr(), prints out GraphQL!
    query MyOp {
      repository(id: "repo1") {
        issues {
          number
          title
        }
      }
    }

    Operations can also have argument (variables), in this case it
    must be named (otherwise a name is created based on root type
    name, such as ``"Query"``):

    >>> from sgqlc.types import Variable
    >>> op = Operation(repo_id=str, reporter_login=str)
    >>> repository = op.repository(id=Variable('repo_id'))
    >>> issues = repository.issues(reporter_login=Variable('reporter_login'))
    >>> issues.__fields__('number', 'title')
    >>> op # or repr(), prints out GraphQL!
    query Query($repoId: String, $reporterLogin: String) {
      repository(id: $repoId) {
        issues(reporterLogin: $reporterLogin) {
          number
          title
        }
      }
    }

    If variable name conflicts with the parameter, you can pass
    them as a single ``variables`` parameter containing a dict.

    >>> from sgqlc.types import Variable
    >>> op = Operation(name='MyOperation', variables={'name': str})
    >>> op.repository(id=Variable('name')).name()
    name
    >>> op # or repr(), prints out GraphQL!
    query MyOperation($name: String) {
      repository(id: $name) {
        name
      }
    }

    Complex argument types are also supported as JSON object (GraphQL names
    and raw types) or actual types:

    >>> op = Operation()
    >>> repository = op.repository(id='sgqlc')
    >>> issues = repository.issues(filter={
    ...     'reporter': [{'nameContains': 'Gustavo'}],
    ...     'startDate': '2019-01-01T00:00:00+00:00',
    ... })
    >>> issues.__fields__('number', 'title')
    >>> op # or repr(), prints out GraphQL!
    query {
      repository(id: "sgqlc") {
        issues(filter: {reporter: [{nameContains: "Gustavo"}], startDate: "2019-01-01T00:00:00+00:00"}) {
          number
          title
        }
      }
    }

    >>> from datetime import datetime, timezone
    >>> from sgqlc.types import global_schema
    >>> op = Operation()
    >>> repository = op.repository(id='sgqlc')
    >>> issues = repository.issues(filter=global_schema.IssuesFilter(
    ...     reporter=[global_schema.ReporterFilterInput(name_contains='Gustavo')],
    ...     start_date=datetime(2019, 1, 1, tzinfo=timezone.utc),
    ... ))
    >>> issues.__fields__('number', 'title')
    >>> op # or repr(), prints out GraphQL!
    query {
      repository(id: "sgqlc") {
        issues(filter: {reporter: [{nameContains: "Gustavo"}], startDate: "2019-01-01T00:00:00+00:00"}) {
          number
          title
        }
      }
    }

    Selectors can be acquired as attributes or items, but they must
    exist in the target type:

    >>> op = Operation()
    >>> op.repository
    Selector(field=repository)
    >>> op['repository']
    Selector(field=repository)
    >>> op.does_not_exist
    Traceback (most recent call last):
      ...
    AttributeError: query {
    } has no field does_not_exist
    >>> op['does_not_exist']
    Traceback (most recent call last):
      ...
    KeyError: 'Query has no field does_not_exist'

    '''  # noqa: E501

    def __init__(self, typ=None, name=None, **args):
        if typ is None:
            typ = global_schema.query_type

        variable_args = OrderedDict()
        if len(args) == 1 and 'variables' in args:
            args = args['variables']
        for k, v in args.items():
            variable_args['$' + k] = v

        if variable_args and not name:
            name = typ.__name__

        self.__type = typ
        self.__kind = self._get_kind()
        self.__name = name
        self.__args = ArgDict(variable_args)
        self.__args._set_container(typ.__schema__, self)
        self.__selection_list = SelectionList(typ)

    def _get_kind(self):
        typ = self.__type
        schema = typ.__schema__
        if schema.query_type is typ:
            return 'query'
        elif schema.mutation_type is typ:
            return 'mutation'
        elif schema.subscription_type is typ:  # pragma: no cover
            return 'subscription'
        else:  # pragma: no cover
            raise ValueError(
                "schema doesn't define %s as query, mutation "
                "or subscription type"
                % (typ.__name__,)
            )

    def __to_graphql__(self, indent=0, indent_string='  ',
                       auto_select_depth=DEFAULT_AUTO_SELECT_DEPTH):
        prefix = indent_string * indent
        kind = self.__kind
        name = ''
        if self.__name:
            name = ' ' + self.__name

        args = self.__args.__to_graphql__(indent, indent_string)
        selections = self.__selection_list.__to_graphql__(
            indent, indent_string, auto_select_depth)

        frags_gql = []
        fragments = self.__selection_list.__collect_fragments__()
        for fragment in fragments.values():
            frags_gql.append(fragment.__to_graphql__(indent, indent_string,
                             auto_select_depth))

        frags = ''
        if frags_gql:
            frags = '\n' + '\n'.join(frags_gql)
        return prefix + kind + name + args + ' ' + selections + frags

    def __iter__(self):
        return iter(self.__selection_list)

    def __len__(self):
        return len(self.__selection_list)

    def __getattr__(self, name):
        try:
            return self.__selection_list[name]
        except KeyError as exc:
            raise AttributeError('%s has no field %s' % (self, name)) from exc

    def __getitem__(self, name):
        return self.__selection_list[name]

    def __str__(self):
        return self.__to_graphql__()

    def __repr__(self):
        return str(self)

    def __bytes__(self):
        return bytes(self.__to_graphql__(indent_string=''), 'utf-8')

    def __add__(self, other):
        errors = other.get('errors')
        ex = None
        if errors:
            ex = GraphQLErrors(errors)

        data = other.get('data')
        if not data:
            if not ex:  # pragma: no cover
                ex = ValueError('no data and no errors')
            raise ex
        o = self.__type(other.get('data'), self.__selection_list)
        o.__errors__ = errors
        return o
