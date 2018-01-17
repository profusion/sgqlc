'''
sgqlc - Simple GraphQL Client
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

:license: ISC
'''

__docformat__ = 'reStructuredText en'

__all__ = ('Operation',)

from collections import OrderedDict

from ..types import ContainerType, ArgDict, global_schema


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
        if issubclass(field.type, ContainerType):
            self.__selection_list = SelectionList(field.type)

    def __len__(self):
        if self.__selection_list is not None:
            return len(self.__selection_list)
        return 1

    def __get_all_fields_selection_list(self):
        q = SelectionList(self.__field__.type)
        for f in self.__field__.type:
            q += Selection(None, f, {})
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
                else:
                    args = {}
            self[n](**args)

    def __to_graphql__(self, indent=0, indent_string='  '):
        prefix = indent_string * indent

        alias = ''
        if self.__alias__:
            alias = self.__alias__ + ': '

        args = self.__field__.args.__to_graphql_input__(
            self.__args__, indent, indent_string)

        query = ''
        if self.__selection_list is not None:
            lst = []
            selections = self.__selection_list
            if not selections:
                selections = self.__get_all_fields_selection_list()
            for s in selections:
                lst.append(s.__to_graphql__(indent + 1, indent_string))
            query = ' {\n%s\n%s}' % ('\n'.join(lst), prefix)
        return prefix + alias + self.__field__.graphql_name + args + query

    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError as exc:
            raise AttributeError('%s has no field %s' % (self, name)) from exc

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
        return self.__to_graphql__()

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
        '__parent', '__field', '__selections',
    )

    def __init__(self, parent, field):
        self.__parent = parent
        self.__field = field
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
                 'Maybe use __alias__ as param?') % (self.__field, s))

        s = self.__selections[alias] = Selection(alias, self.__field, args)
        self.__parent += s
        return s

    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError as exc:
            raise AttributeError('%s has no field %s' % (self, name)) from exc

    def __getitem__(self, name):
        selection = self()
        if name == '__fields__':
            return selection.__fields__
        return selection[name]

    def __str__(self):
        return '%s(field=%s)' % (self.__class__.__name__, self.__field)

    def __repr__(self):
        return str(self)


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

    '''

    __slots__ = ('__type', '__selectors', '__selections')

    def __init__(self, typ):
        assert issubclass(typ, ContainerType), str(typ) + ': not a container'
        self.__type = typ
        self.__selectors = {}
        self.__selections = []

    def __str__(self):
        return self.__to_graphql__()

    def __repr__(self):
        return self.__to_graphql__()

    def __bytes__(self):
        return bytes(self.__to_graphql__(indent_string=''), 'utf-8')

    def __to_graphql__(self, indent=0, indent_string='  '):
        prefix = indent_string * indent

        s = ['{']
        for v in self.__selections:
            s.append(v.__to_graphql__(indent + 1, indent_string))

        s.append(prefix + '}')
        return '\n'.join(s)

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


class Operation:
    '''GraphQL Operation: query or mutation.

    The given type must be one of ``schema.Query`` or
    ``schema.Mutation``, defaults to ``global_schema.Query``.

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

    '''
    def __init__(self, typ=None, name=None, **args):
        if typ is None:
            typ = global_schema.Query

        variable_args = OrderedDict()
        for k, v in args.items():
            variable_args['$' + k] = v

        if variable_args and not name:
            name = typ.__name__

        self.__type = typ
        self.__name = name
        self.__args = ArgDict(variable_args)
        self.__args._set_container(typ.__schema__, self)
        self.__selection_list = SelectionList(typ)

    def __to_graphql__(self, indent=0, indent_string='  '):
        prefix = indent_string * indent
        kind = 'query'
        if self.__type.__name__ == 'Mutation':
            kind = 'mutation'

        name = ''
        if self.__name:
            name = ' ' + self.__name

        args = self.__args.__to_graphql__(indent, indent_string)
        selections = self.__selection_list.__to_graphql__(
            indent, indent_string)
        return prefix + kind + name + args + ' ' + selections

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
        return self.__to_graphql__()

    def __bytes__(self):
        return bytes(self.__to_graphql__(indent_string=''), 'utf-8')

    def __add__(self, other):
        return self.__type(other.get('data'), self.__selection_list)
