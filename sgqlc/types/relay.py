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
