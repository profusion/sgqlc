'''
sgqlc - Simple GraphQL Client
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

GraphQL Types for `Relay <https://facebook.github.io/relay/>`_
==============================================================

Exposes ``Node`` and ``Connection``, matching `Global Object
Identification
<https://facebook.github.io/relay/graphql/objectidentification.htm>`_
and `Cursor Connections
<https://facebook.github.io/relay/graphql/connections.htm>`_, which
are widely used.

Examples
--------

>>> from sgqlc.types import Type, Field, list_of
>>> class NodeBasedInterface(Node):
...     a_int = int
...
>>> NodeBasedInterface # or repr()
interface NodeBasedInterface implements Node {
  id: ID!
  aInt: Int
}
>>> class NodeBasedType(Type, Node):
...     a_int = int
...
>>> NodeBasedType # or repr()
type NodeBasedType implements Node {
  id: ID!
  aInt: Int
}

:class:`Connection` subclasses will get ``page_info`` and
``total_count``, as well as ``__iadd__`` to merge 2 connections:

>>> class MyEdge(Type):
...     node = NodeBasedType
...     cursor = str
...
>>> class MyConn(Connection):
...    nodes = list_of(NodeBasedType)
...    edges = list_of(MyEdge)
...
>>> MyConn # or repr()
type MyConn {
  pageInfo: PageInfo!
  totalCount: Int
  nodes: [NodeBasedType]
  edges: [MyEdge]
}
>>> class MyTypeWithConn(Type):
...     conn = Field(MyConn, args=connection_args())
...
>>> MyTypeWithConn # or repr()
type MyTypeWithConn {
  conn(
    after: String
    before: String
    first: Int
    last: Int
  ): MyConn
}

Given ``json_data1`` being the contents of the GraphQL query::

   query {
      getMyTypeWithConn(id: "...") {
        conn(first: 2) { # first page
          pageInfo { startCursor, endCursor, hasNextPage, hasPreviousPage }
          totalCount
          nodes { id, aInt }
          edges { cursor, node { id, aInt } }
        }
      }
   }

>>> json_data1 = { # page 1 (2 elements of 4)
...     'pageInfo': {
...         'startCursor': 'cursor-1',
...         'endCursor': 'cursor-2',
...         'hasNextPage': True,
...         'hasPreviousPage': False,
...     },
...     'totalCount': 4,
...     'nodes': [
...         {'id': '1111', 'aInt': 1},
...         {'id': '2222', 'aInt': 2},
...     ],
...     'edges': [
...         {'cursor': 'cursor-1', 'node': {'id': '1111', 'aInt': 1}},
...         {'cursor': 'cursor-2', 'node': {'id': '2222', 'aInt': 2}},
...     ],
... }
>>> conn1 = MyConn(json_data1)
>>> print(conn1.page_info)  # doctest: +ELLIPSIS
PageInfo(end_cursor=cursor-2, start_cursor=cursor-1, has_next_page=True...
>>> print(conn1.total_count)
4
>>> for n in conn1.nodes:
...     print(repr(n))
NodeBasedType(id='1111', a_int=1)
NodeBasedType(id='2222', a_int=2)
>>> for e in conn1.edges:
...     print(repr(e))
MyEdge(node=NodeBasedType(id='1111', a_int=1), cursor='cursor-1')
MyEdge(node=NodeBasedType(id='2222', a_int=2), cursor='cursor-2')


We'd execute the query to fetch the second page as ``json_data2``::

   query {
      getMyTypeWithConn(id: "...") {
        conn(first: 2, after: "cursor-2") { # second page
          pageInfo { startCursor, endCursor, hasNextPage, hasPreviousPage }
          totalCount
          nodes { id, aInt }
          edges { cursor, node { id, aInt } }
        }
      }
   }

>>> json_data2 = { # page 2 (2 elements of 4)
...     'pageInfo': {
...         'startCursor': 'cursor-3',
...         'endCursor': 'cursor-4',
...         'hasNextPage': False,
...         'hasPreviousPage': True,
...     },
...     'totalCount': 4,
...     'nodes': [
...         {'id': '3333', 'aInt': 3},
...         {'id': '4444', 'aInt': 4},
...     ],
...     'edges': [
...         {'cursor': 'cursor-3', 'node': {'id': '3333', 'aInt': 3}},
...         {'cursor': 'cursor-4', 'node': {'id': '4444', 'aInt': 4}},
...     ],
... }
>>> conn2 = MyConn(json_data2)
>>> print(conn2.page_info)  # doctest: +ELLIPSIS
PageInfo(end_cursor=cursor-4, start_cursor=cursor-3, has_next_page=False...
>>> print(conn2.total_count)
4
>>> for n in conn2.nodes:
...     print(repr(n))
NodeBasedType(id='3333', a_int=3)
NodeBasedType(id='4444', a_int=4)
>>> for e in conn2.edges:
...     print(repr(e))
MyEdge(node=NodeBasedType(id='3333', a_int=3), cursor='cursor-3')
MyEdge(node=NodeBasedType(id='4444', a_int=4), cursor='cursor-4')

One can merge ``conn2`` into ``conn1``, also updating its backing
store ``json_data1``:

>>> conn1 += conn2
>>> print(conn1.page_info)  # doctest: +ELLIPSIS
PageInfo(end_cursor=cursor-4, start_cursor=cursor-1, has_next_page=False...
>>> print(conn1.total_count)
4
>>> for n in conn1.nodes:
...     print(repr(n))
NodeBasedType(id='1111', a_int=1)
NodeBasedType(id='2222', a_int=2)
NodeBasedType(id='3333', a_int=3)
NodeBasedType(id='4444', a_int=4)
>>> for e in conn1.edges:
...     print(repr(e))
MyEdge(node=NodeBasedType(id='1111', a_int=1), cursor='cursor-1')
MyEdge(node=NodeBasedType(id='2222', a_int=2), cursor='cursor-2')
MyEdge(node=NodeBasedType(id='3333', a_int=3), cursor='cursor-3')
MyEdge(node=NodeBasedType(id='4444', a_int=4), cursor='cursor-4')
>>> import json
>>> print(json.dumps(json_data1, sort_keys=True, indent=2))
{
  "edges": [
    {
      "cursor": "cursor-1",
      "node": {
        "aInt": 1,
        "id": "1111"
      }
    },
    {
      "cursor": "cursor-2",
      "node": {
        "aInt": 2,
        "id": "2222"
      }
    },
    {
      "cursor": "cursor-3",
      "node": {
        "aInt": 3,
        "id": "3333"
      }
    },
    {
      "cursor": "cursor-4",
      "node": {
        "aInt": 4,
        "id": "4444"
      }
    }
  ],
  "nodes": [
    {
      "aInt": 1,
      "id": "1111"
    },
    {
      "aInt": 2,
      "id": "2222"
    },
    {
      "aInt": 3,
      "id": "3333"
    },
    {
      "aInt": 4,
      "id": "4444"
    }
  ],
  "pageInfo": {
    "endCursor": "cursor-4",
    "hasNextPage": false,
    "hasPreviousPage": false,
    "startCursor": "cursor-1"
  },
  "totalCount": 4
}

When merging, the receiver connection can be empty:

>>> json_data0 = {}
>>> conn0 = MyConn(json_data0)
>>> conn0 += conn1
>>> print(conn0.page_info)  # doctest: +ELLIPSIS
PageInfo(end_cursor=cursor-4, start_cursor=cursor-1, has_next_page=False...
>>> print(conn0.total_count)
4
>>> for n in conn0.nodes:
...     print(repr(n))
NodeBasedType(id='1111', a_int=1)
NodeBasedType(id='2222', a_int=2)
NodeBasedType(id='3333', a_int=3)
NodeBasedType(id='4444', a_int=4)
>>> for e in conn0.edges:
...     print(repr(e))
MyEdge(node=NodeBasedType(id='1111', a_int=1), cursor='cursor-1')
MyEdge(node=NodeBasedType(id='2222', a_int=2), cursor='cursor-2')
MyEdge(node=NodeBasedType(id='3333', a_int=3), cursor='cursor-3')
MyEdge(node=NodeBasedType(id='4444', a_int=4), cursor='cursor-4')
>>> print(json.dumps(json_data0, sort_keys=True, indent=2))
{
  "edges": [
    {
      "cursor": "cursor-1",
      "node": {
        "aInt": 1,
        "id": "1111"
      }
    },
    {
      "cursor": "cursor-2",
      "node": {
        "aInt": 2,
        "id": "2222"
      }
    },
    {
      "cursor": "cursor-3",
      "node": {
        "aInt": 3,
        "id": "3333"
      }
    },
    {
      "cursor": "cursor-4",
      "node": {
        "aInt": 4,
        "id": "4444"
      }
    }
  ],
  "nodes": [
    {
      "aInt": 1,
      "id": "1111"
    },
    {
      "aInt": 2,
      "id": "2222"
    },
    {
      "aInt": 3,
      "id": "3333"
    },
    {
      "aInt": 4,
      "id": "4444"
    }
  ],
  "pageInfo": {
    "endCursor": "cursor-4",
    "hasNextPage": false,
    "hasPreviousPage": false,
    "startCursor": "cursor-1"
  },
  "totalCount": 4
}



:license: ISC
'''

__docformat__ = 'reStructuredText en'

__all__ = ('Node', 'PageInfo', 'Connection', 'connection_args')

from . import Type, Interface, non_null, ArgDict, String, Int


class Node(Interface):
    '''Global Object Identification based on Relay specification.

    https://facebook.github.io/relay/graphql/objectidentification.htm
    '''
    id = non_null(id)  # noqa: A003


class PageInfo(Type):
    ''':class:`Connection` page information.

    https://facebook.github.io/relay/graphql/connections.htm
    '''
    end_cursor = str
    start_cursor = str
    has_next_page = non_null(bool)
    has_previous_page = non_null(bool)


class Connection(Type):
    '''Cursor Connections based on Relay specification.

    https://facebook.github.io/relay/graphql/connections.htm

    .. note::

      This class exposes ``+=`` (in-place addition) operator to append
      information from another connection into this. The usage is as
      follow, if ``obj.connection.page_info.has_next_page``, then you
      should query the next page using
      ``after=obj.connection.page_info.end_cursor``. The resulting
      object should be ``obj.connection += obj2.connection``, this
      will add the contents of ``obj2.connection`` to
      ``obj.connection``, resetting
      ``obj.connection.page_info.has_next_page``,
      ``obj.connection.page_info.end_cursor`` and
      ``obj.connection.total_count``. These changes will be applied to
      the JSON backing store, if any.
    '''
    __auto_register = False  # do not expose this in Schema, just subclasses
    page_info = non_null(PageInfo)
    total_count = int

    def __iadd__(self, other):
        # NOTE: assign to list, not '+=', so ContainerType.__setattr__()
        # is called to apply to backing store
        has_self_nodes = hasattr(self, 'nodes') and self.nodes is not None
        has_other_nodes = hasattr(other, 'nodes') and other.nodes is not None
        if has_self_nodes and has_other_nodes:
            self.nodes = self.nodes + other.nodes
        elif has_other_nodes:
            self.nodes = other.nodes

        has_self_edges = hasattr(self, 'edges') and self.edges is not None
        has_other_edges = hasattr(other, 'edges') and other.edges is not None
        if has_self_edges and has_other_edges:
            self.edges = self.edges + other.edges
        elif has_other_edges:
            self.edges = other.edges

        has_other_total_count = hasattr(other, 'total_count') and \
            other.total_count is not None
        if has_other_total_count:
            self.total_count = other.total_count

        has_self_page_info = hasattr(self, 'page_info') and \
            self.page_info is not None
        has_other_page_info = hasattr(other, 'page_info') and \
            other.page_info is not None
        if has_self_page_info and has_other_page_info:
            self.page_info.end_cursor = other.page_info.end_cursor
            self.page_info.has_next_page = other.page_info.has_next_page
        elif has_other_page_info:
            self.page_info = other.page_info

        return self


def connection_args(*lst, **mapping):
    '''Returns the default parameters for connection.

    Extra parameters may be given as argument, both as iterable,
    positional tuples or mapping.

    By default, provides:

     - ``after: String``
     - ``before: String``
     - ``first: Int``
     - ``last: Int``
    '''
    pd = ArgDict(*lst, **mapping)
    pd.setdefault('after', String)
    pd.setdefault('before', String)
    pd.setdefault('first', Int)
    pd.setdefault('last', Int)
    return pd
