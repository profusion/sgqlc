import argparse
import json
import re
import sys

from collections import OrderedDict
from typing import List, NamedTuple, Union

from sgqlc.types import BaseItem

from graphql.language.source import Source
from graphql.language.parser import parse as parse_graphql
from graphql.language.visitor import Visitor, visit


__docformat__ = 'reStructuredText en'


to_python_name = BaseItem._to_python_name


def format_graphql_type(typ):
    kind = typ['kind']
    if kind == 'NON_NULL':
        of_type = typ['ofType']
        return '%s!' % (format_graphql_type(of_type),)
    elif kind == 'LIST':
        of_type = typ['ofType']
        return '[%s]' % (format_graphql_type(of_type),)
    else:
        return typ['name']


def is_value_required(field):
    return field['type']['kind'] == 'NON_NULL' \
        and field.get('defaultValue')


class Variable:
    def __init__(self, name):
        self.name = name
        self.type = None
        self.default_value = None
        self.node = None
        self.usage = 0

    def __repr__(self):
        return 'sgqlc.types.Variable(%r)' % (self.name,)


# Use Null instead of None as Visitor.leave_* understands None as IDLE,
# which keeps the original node.
class Null:
    def __repr__(self):
        return 'None'


class NoValidation:
    def get_operation_type(self, operation_name):
        return None

    def get_type(self, type_name):
        return None

    def get_type_field(self, typ, field_name):
        return None

    def get_field_argument(self, field, argument_name):
        return None

    def unwrap_type(self, typ):
        return None

    def validate_type(self, typ, candidate, value):
        return None

    def validate_object(typ, candidate_name):
        return None

    def validate_input_object_fields(self, typ, obj):
        return None

    def validate_type_matches(self, typ, candidate):
        return None

    def validate_variable_definition(self, definition):
        return None


class SchemaValidation(NoValidation):
    def __init__(self, schema):
        self.schema = schema
        self.types = sorted(schema['types'], key=lambda x: x['name'])
        self.type_by_name = {
            t['name']: self._create_type(t) for t in self.types
        }
        self.operations = {
            'query': self._get_path('queryType', 'name'),
            'mutation': self._get_path('mutationType', 'name'),
            'subscription': self._get_path('subscriptionType', 'name'),
        }

    def _get_path(self, *path, fallback=None):
        d = self.schema
        path = list(path)
        while d and path:
            d = d.get(path.pop(0))

        if d is None:
            return fallback
        return d

    def _create_type(self, typ):
        fields = typ.get('fields') or typ.get('inputFields') or []
        typ['fields'] = {
            f['name']: self._create_field(f) for f in fields
        }
        if 'inputFields' in typ:
            del typ['inputFields']

        enum_values = typ['enumValues'] or []
        typ['enumValues'] = {e['name'] for e in enum_values}

        possible_types = typ['possibleTypes'] or typ['interfaces'] or []
        typ['possibleTypes'] = {t['name'] for t in possible_types}

        return typ

    def _create_field(self, field):
        args = field.get('args') or []
        field['args'] = {
            a['name']: a for a in args
        }
        return field

    def get_operation_type(self, operation_name):
        type_name = self.operations[operation_name]
        return self.type_by_name[type_name]

    def get_type(self, type_name):
        return self.type_by_name[type_name]

    @staticmethod
    def get_type_field(typ, field_name):
        return typ['fields'][field_name]

    @staticmethod
    def get_field_argument(field, argument_name):
        return field['args'][argument_name]

    @staticmethod
    def unwrap_type(typ):
        while typ.get('ofType'):
            typ = typ['ofType']
        return typ

    @staticmethod
    def validate_non_null(candidate_name):
        if candidate_name == 'Null':
            raise ValueError('got null where non-null is required')

    type_alternatives = {
        'ID': ('Int', 'String'),
        'Float': ('Int',),
    }
    builtin_types = ('Int', 'Float', 'String', 'Boolean', 'ID')
    accepted_user_scalars = ('String',)

    @classmethod
    def validate_scalar(cls, name, candidate_name):
        if name == candidate_name:
            return
        alternatives = cls.type_alternatives.get(name, ())
        if candidate_name in alternatives:
            return

        # user-defined scalars are usually defined as strings
        if name not in cls.builtin_types and \
                candidate_name in cls.accepted_user_scalars:
            return
        raise ValueError('got %s where %s is required' %
                         (candidate_name, name))

    def validate_enum(self, name, candidate_name, value):
        if candidate_name != 'Enum':
            raise ValueError('got %s where %s is required' %
                             (candidate_name, name))
        enum = self.get_type(name)
        if value not in enum['enumValues']:
            raise ValueError('enum %s has no value %s' % (name, value))

    def validate_type(self, typ, candidate_name, value):
        while typ:
            kind = typ['kind']
            name = typ.get('name')
            if kind == 'NON_NULL':
                self.validate_non_null(candidate_name)
            elif value is None or isinstance(value, Null):
                return
            elif kind == 'LIST':
                pass
            elif kind == 'SCALAR':
                self.validate_scalar(name, candidate_name)
                return
            elif kind == 'ENUM':
                self.validate_enum(name, candidate_name, value)
                return
            elif kind == 'OBJECT' or kind == 'INPUT_OBJECT':
                self.validate_object(typ, candidate_name)
                return
            else:
                raise ValueError('cannot validate kind=%s' % (kind,))
            typ = typ.get('ofType')

    @staticmethod
    def validate_object(typ, candidate_name):
        name = typ['name']
        if candidate_name != name:
            raise ValueError('got %s where %s is required' %
                             (candidate_name, name))

    def validate_input_object_fields(self, typ, obj):
        required = set()
        name = self.unwrap_type(typ)['name']
        fields = self.get_type(name)['fields']
        for f in fields.values():
            if is_value_required(f):
                required.add(f['name'])

        for name in obj.keys():
            if name in required:
                required.remove(name)

        if required:
            raise ValueError('missing required fields of type %s: %s' %
                             (typ['name'], ', '.join(required)))

    @staticmethod
    def validate_type_matches(typ, candidate):
        used = format_graphql_type(candidate)
        required = format_graphql_type(typ)
        if not required.endswith('!'):
            used = used.rstrip('!')  # relax candidate type

        if required != used:
            msg = 'got %s where %s is required' % (
                format_graphql_type(candidate),
                required,
            )
            raise ValueError(msg)

    def validate_variable_definition(self, definition):
        if definition.type['kind'] == 'NON_NULL' and definition.default_value:
            raise ValueError('non-null variables can\'t have default value')


class SelectionFormatResult(NamedTuple):
    lines: List[str]
    idx: int


class ParsedSchemaName(NamedTuple):
    path: Union[str, None]
    modname: str
    sym: str

    def __str__(self):
        return '%s.%s' % (self.modname, self.sym)

    _parse_regex = re.compile(
        '^(?P<path>[.]*)(?P<modname>[^:]+)(?:|(:(?P<sym>[a-zA-Z0-9_]+)))$'
    )

    @classmethod
    def parse_schema_name(cls, schema_name):
        '''
        >>> ParsedSchemaName.parse_schema_name('schema')
        ParsedSchemaName(path=None, modname='schema', sym='schema')
        >>> ParsedSchemaName.parse_schema_name('schema:sym')
        ParsedSchemaName(path=None, modname='schema', sym='sym')
        >>> ParsedSchemaName.parse_schema_name('..schema:sym')
        ParsedSchemaName(path='..', modname='schema', sym='sym')
        >>> ParsedSchemaName.parse_schema_name('..schema')
        ParsedSchemaName(path='..', modname='schema', sym='schema')
        '''
        m = cls._parse_regex.match(schema_name)
        if not m:
            raise ValueError('invalid schema_name format')

        path = m.group('path') or None
        modname = m.group('modname')
        sym = m.group('sym') or modname
        return cls(path, modname, sym)


class GraphQLToPython(Visitor):
    def __init__(self, validation, schema_name, short_names):
        self.validation = validation
        self.schema_name = schema_name
        self.short_names = short_names
        self.type_stack = []
        self.field_stack = []
        self.variables = {}
        self.current_variable_definition = None

    @staticmethod
    def leave_name(node, *_args):
        return node.value

    def leave_variable(self, node, *_args):
        name = node.name
        if not self.current_variable_definition:
            try:
                v = self.variables[name]
            except KeyError as ex:
                self.report_unknown_variable(node, ex)
            self.validation.validate_type_matches(self.type_stack[-1], v.type)
            v.usage += 1
            return v

        v = self.current_variable_definition
        v.name = name
        self.variables[name] = v
        return v

    def leave_document(self, node, *_args):
        unused = []
        for v in self.variables.values():
            if v.usage == 0:
                unused.append(v)
        if unused:
            self.report_unused_variables(unused)
        return node.definitions

    def selection_name(self, parent, name, idx):
        if self.short_names:
            return '_sel%d' % (idx,)
        else:
            return '%s_%s' % (parent, name)

    def format_selection_set_field(self, parent, name, selection,
                                   children, lines, idx):
        field_selection = '%s.%s' % (parent, selection)
        if not children:
            lines.append(field_selection)
            return SelectionFormatResult(lines, idx)

        sel = self.selection_name(parent, name, idx)
        idx += 1

        lines.append('%s = %s' % (sel, field_selection))
        return self.format_selection_set(sel, children, lines, idx)

    def format_selection_set_inline_fragment(self, parent, type_condition,
                                             children, lines, idx):
        sel = self.selection_name(parent, '_as__%s' % type_condition, idx)
        type_condition = self.format_typename_usage(type_condition)
        idx += 1
        lines.append('%s = %s.__as__(%s)' % (sel, parent, type_condition))
        return self.format_selection_set(sel, children, lines, idx)

    @staticmethod
    def format_selection_set_fragment_spread(parent, name, lines, idx):
        # call fragment function instead of Fragment.{name}
        # as Fragment wasn't defined yet and it may contain circular
        # dependencies
        lines.append('%s.__fragment__(fragment_%s())' % (parent, name))
        return SelectionFormatResult(lines, idx)

    wrapper_map = {
        'NON_NULL': 'sgqlc.types.non_null',
        'LIST': 'sgqlc.types.list_of',
    }

    @staticmethod
    def format_typename_usage(typename):
        return '%s.%s' % ('_schema', typename)

    def format_type_usage(self, typ):
        wrapper = self.wrapper_map.get(typ['kind'])
        if wrapper:
            return '%s(%s)' % (wrapper, self.format_type_usage(typ['ofType']))

        return self.format_typename_usage(typ['name'])

    def format_variable_definition(self, node):
        name = node.variable.name
        typedef = self.format_type_usage(node.type)
        defval = ''
        if node.default_value:
            defval = ', default=%r' % (node.default_value,)
        return (name, 'sgqlc.types.Arg(%s%s)' % (typedef, defval))

    def format_args_definitions(self, variable_definitions):
        result = OrderedDict()
        for d in variable_definitions:
            k, v = self.format_variable_definition(d)
            result[k] = v
        return ', '.join('%s=%s' % r for r in result.items())

    def format_selection_set(self, parent, selection_set, lines, idx):
        for kind, *rest in selection_set:
            if kind == 'field':
                name, selection, children = rest
                _, idx = self.format_selection_set_field(
                    parent, name, selection, children, lines, idx,
                )
            elif kind == 'inline_fragment':
                type_condition, children = rest
                _, idx = self.format_selection_set_inline_fragment(
                    parent, type_condition, children, lines, idx,
                )
            elif kind == 'fragment':
                name, = rest
                _, idx = self.format_selection_set_fragment_spread(
                    parent, name, lines, idx,
                )

        return SelectionFormatResult(lines, idx)

    @classmethod
    def selection_set_has_fragments(cls, selection_set):
        if not selection_set:
            return False

        for kind, *rest in selection_set:
            if kind == 'field':
                _, _, children = rest
                if cls.selection_set_has_fragments(children):
                    return True
            elif kind == 'inline_fragment':
                _, children = rest
                if cls.selection_set_has_fragments(children):
                    return True
            elif kind == 'fragment':
                return True

        return False

    @staticmethod
    def get_node_location(node):
        source = node.loc.source
        loc = source.get_location(node.loc.start)
        return '%s:%d:%d' % (source.name, loc.line, loc.column)

    @classmethod
    def report_type_validation(cls, node, ex):
        loc = cls.get_node_location(node)
        raise SystemExit('no type named %s at %s' % (ex, loc)) from ex

    @classmethod
    def report_type_field_validation(cls, node, typ, ex):
        loc = cls.get_node_location(node)
        type_name = typ['name']
        raise SystemExit('no field named %s on type %s at %s' %
                         (ex, type_name, loc)) from ex

    @classmethod
    def report_field_argument_validation(cls, node, typ, field, ex):
        loc = cls.get_node_location(node)
        field_name = field['name']
        type_name = typ['name']
        raise SystemExit('no argument named %s on field %s.%s at %s' %
                         (ex, type_name, field_name, loc)) from ex

    @classmethod
    def report_possible_type_validation(cls, node, typ, type_name):
        loc = cls.get_node_location(node)
        raise SystemExit('type %s not possible for %s at %s' %
                         (type_name, typ['name'], loc))

    @classmethod
    def report_unknown_variable(cls, node, ex):
        loc = cls.get_node_location(node)
        raise SystemExit('no variable named %s at %s' % (ex, loc)) from ex

    @classmethod
    def report_validation_error(cls, node, ex):
        loc = cls.get_node_location(node)
        raise SystemExit('validation failed: %s at %s' % (ex, loc)) from ex

    @classmethod
    def report_variable_definition(cls, node, ex):
        loc = cls.get_node_location(node)
        raise SystemExit('invalid variable definition: %s at %s' %
                         (ex, loc)) from ex

    @classmethod
    def report_unused_variables(cls, variables):
        s = ', '.join(
            '%s at %s' % (v.name, cls.get_node_location(v.node))
            for v in variables
        )
        raise SystemExit('unused variable definitions: %s' % (s,))

    def enter_operation_definition(self, node, *_args):
        try:
            operation = node.operation.value
            typ = self.validation.get_operation_type(operation)
            self.type_stack.append(typ)
        except KeyError as ex:
            self.report_type_validation(node, ex)

    def leave_operation_definition(self, node, *_args):
        args_definition = self.format_args_definitions(
            node.variable_definitions or [],
        )
        if args_definition:
            args_definition = ', variables=dict(%s)' % (args_definition,)
        lines = [
            '_op = sgqlc.operation.Operation'
            '(_schema_root.%s_type, name=%r%s)' % (
                node.operation.value,
                node.name, args_definition),
        ]
        self.format_selection_set('_op', node.selection_set, lines, 0)
        lines.append('return _op')
        self.type_stack.pop()
        name = to_python_name(node.name)
        return (node.operation.value, name, '''\
def %(operation)s_%(name)s():
    %(lines)s
''' % {
            'operation': node.operation.value,
            'name': name,
            'lines': '\n    '.join(lines),
        })

    def enter_fragment_definition(self, node, *_args):
        try:
            typ = self.validation.get_type(node.type_condition.name.value)
            self.type_stack.append(typ)
        except KeyError as ex:
            self.report_type_validation(node, ex)

    def leave_fragment_definition(self, node, *_args):
        lines = []
        self.format_selection_set('_frag', node.selection_set, lines, 0)
        lines.append('return _frag')
        self.type_stack.pop()
        name = to_python_name(node.name)
        return ('fragment', name, '''\
def fragment_%(name)s():
    _frag = sgqlc.operation.Fragment(%(type)s, %(gql_name)r)
    %(lines)s
''' % {
            'name': name,
            'gql_name': node.name,
            'type': self.format_typename_usage(node.type_condition['name']),
            'lines': '\n    '.join(lines)
        })

    @staticmethod
    def leave_selection_set(node, *_args):
        return node.selections

    def enter_variable_definition(self, node, *_args):
        self.current_variable_definition = Variable('<unknown>')
        self.current_variable_definition.node = node
        self.type_stack.append(None)

    def leave_variable_definition(self, node, *_args):
        v = self.current_variable_definition
        v.type = node.type
        v.default_value = node.default_value
        try:
            self.validation.validate_variable_definition(v)
        except Exception as ex:
            self.report_variable_definition(node, ex)
        self.current_variable_definition = None
        self.type_stack.pop()

    def set_variable_definition_type(self, typ):
        if not self.current_variable_definition:
            return
        self.current_variable_definition.type = typ
        self.type_stack[-1] = typ

    def leave_non_null_type(self, node, *_args):
        typ = {'kind': 'NON_NULL', 'name': None, 'ofType': node.type}
        self.set_variable_definition_type(typ)
        return typ

    def leave_list_type(self, node, *_args):
        typ = {'kind': 'LIST', 'name': None, 'ofType': node.type}
        self.set_variable_definition_type(typ)
        return typ

    def leave_named_type(self, node, *_args):
        try:
            name = node.name
            typ = self.validation.get_type(name)
            if not typ:
                # fallback when validation is not being used
                typ = {'kind': 'SCALAR', 'name': name, 'ofType': None}
            self.set_variable_definition_type(typ)
            return typ

        except KeyError as ex:
            self.report_type_validation(node, ex)

    def enter_field(self, node, *_args):
        typ = self.type_stack[-1]
        try:
            field = self.validation.get_type_field(typ, node.name.value)
            self.field_stack.append(field)
            if not field:
                self.type_stack.append(None)
                return
            inner_type = self.validation.unwrap_type(field['type'])
            type_name = inner_type['name']
            typ = self.validation.get_type(type_name)
            self.type_stack.append(typ)
        except KeyError as ex:
            self.report_type_field_validation(node, typ, ex)

    def validate_required_arguments(self, node):
        field = self.field_stack[-1]
        if not field:
            return
        required = set()
        for a in field['args'].values():
            if is_value_required(a):
                required.add(a['name'])

        for name, _ in node.arguments:
            if name in required:
                required.remove(name)

        if required:
            raise ValueError(
                'missing required arguments: %s at %s' %
                (', '.join(required), self.get_node_location(node))
            )

    def leave_field(self, node, *_args):
        self.validate_required_arguments(node)

        args = node.arguments
        alias = ''
        if node.alias:
            alias = to_python_name(node.alias)
            args = list(args) + [('__alias__', alias)]

        name = to_python_name(node.name)
        selection = '%(name)s(%(args)s)' % {
            'name': name,
            'args': ', '.join('%s=%r' % a for a in args),
        }
        if not alias:
            alias = name
        children = node.selection_set
        self.type_stack.pop()
        self.field_stack.pop()

        return ('field', alias, selection, children)

    def enter_argument(self, node, *_args):
        typ = self.type_stack[-2]
        field = self.field_stack[-1]
        try:
            name = node.name.value
            arg = self.validation.get_field_argument(field, name)
            if not arg:
                self.type_stack.append(None)
                return
            self.type_stack.append(arg['type'])
        except KeyError as ex:
            self.report_field_argument_validation(node, typ, field, ex)

    def leave_argument(self, node, *_args):
        self.type_stack.pop()
        return (to_python_name(node.name), node.value)

    @staticmethod
    def leave_fragment_spread(node, *_args):
        return ('fragment', to_python_name(node.name))

    def enter_inline_fragment(self, node, *_args):
        typ = self.type_stack[-1]
        if not typ:
            self.type_stack.append(None)
            return
        type_name = node.type_condition.name.value
        if type_name not in typ['possibleTypes']:
            self.report_possible_type_validation(node, typ, type_name)

        try:
            typ = self.validation.get_type(type_name)
            self.type_stack.append(typ)
        except KeyError as ex:
            self.report_type_validation(node, ex)

    def leave_inline_fragment(self, node, *_args):
        self.type_stack.pop()
        return ('inline_fragment', node.type_condition['name'],
                node.selection_set)

    def validate_value(self, node, candidate_type, value):
        try:
            self.validation.validate_type(
                self.type_stack[-1],
                candidate_type,
                value,
            )
        except Exception as ex:
            self.report_validation_error(node, ex)

    def leave_int_value(self, node, *_args):
        value = int(node.value)
        self.validate_value(node, 'Int', value)
        return value

    def leave_float_value(self, node, *_args):
        value = float(node.value)
        self.validate_value(node, 'Float', value)
        return value

    def leave_string_value(self, node, *_args):
        value = node.value
        self.validate_value(node, 'String', value)
        return value

    def leave_boolean_value(self, node, *_args):
        value = node.value
        self.validate_value(node, 'Boolean', value)
        return value

    def leave_null_value(self, node, *_args):
        value = Null()  # can't return None due Visitor() pattern
        self.validate_value(node, 'Null', value)
        return value

    def leave_enum_value(self, node, *_args):
        value = node.value
        self.validate_value(node, 'Enum', value)
        return value

    @staticmethod
    def leave_list_value(node, *_args):
        return node.values

    def leave_object_value(self, node, *_args):
        value = dict(node.fields)
        try:
            self.validation.validate_input_object_fields(
                self.type_stack[-1],
                value,
            )
        except Exception as ex:
            self.report_validation_error(node, ex)
        return value

    def enter_object_field(self, node, *_args):
        typ = self.type_stack[-1]
        if not typ:
            self.type_stack.append(None)
            return
        try:
            name = node.name.value
            inner_type = self.validation.unwrap_type(typ)
            typ = self.validation.get_type(inner_type['name'])
            field = self.validation.get_type_field(typ, name)
            self.type_stack.append(field['type'])
        except KeyError as ex:
            self.report_type_field_validation(node, typ, ex)

    def leave_object_field(self, node, *_args):
        self.type_stack.pop()
        return (node.name, node.value)


class CodeGen:
    def __init__(self, schema, schema_name, operations_gql,
                 writer, short_names):
        '''
        :param schema: if provided (not ``None``), will do validation
          using :class:`SchemaValidation`, otherwise no validation
          is done. It must be an introspection query result, usually
          loaded from a JSON file.
        :type schema: dict or None

        :param schema_name: where to look for SGQLC schema.
        :type schema_name: :class:`ParsedSchemaName`

        :param operations_gql: a sequence of
          :class:`graphql.language.source.Source` to parse.
        :type operations_gql: list of :class:`graphql.language.source.Source`

        :param writer: function used to output strings.
        :type writer: function that receives a str and returns nothing

        :param short_names: if ``True``, selection names will be short,
          using a sequential index rather than the name prefix. This
          improves loading huge files at the expense of readability.
        :type short_names: bool
        '''
        self.schema = schema
        self.schema_name = schema_name
        self.operations_gql = operations_gql
        self.writer = writer
        self.short_names = short_names

        if schema:
            self.validation = SchemaValidation(schema)
        else:
            self.validation = NoValidation()

    def write(self):
        self.write_header()
        self.write_operations()

    def write_header(self):
        self.writer('import sgqlc.types\n')
        self.writer('import sgqlc.operation\n')
        if self.schema_name.path:
            self.writer('from %s import %s' %
                        (self.schema_name.path, self.schema_name.modname))
        else:
            self.writer('import ' + self.schema_name.modname)
        self.writer('''

_schema = %s
_schema_root = _schema.%s

__all__ = ('Operations',)
''' % (self.schema_name.modname, self.schema_name.sym))

    def write_operations(self):
        for source in self.operations_gql:
            self.write_operation(source)

    def write_operation(self, source):
        gql = parse_graphql(source)
        kind_operations = {}
        visitor = GraphQLToPython(
            self.validation,
            self.schema_name,
            self.short_names,
        )
        for kind, name, code in visit(gql, visitor):
            kind_operations.setdefault(kind, []).append((name, code))

        # sort so fragments come first (fragment, mutation, query)
        kinds = []
        for kind, code_list in sorted(kind_operations.items()):
            names = []
            for name, code in code_list:
                self.writer('\n\n')
                self.writer(code)
                names.append(name)

            kinds.append(kind)
            self.writer('\n\nclass %s:\n' % (kind.title(),))
            for name in sorted(names):
                self.writer('    %s = %s_%s()\n' % (name, kind, name))

        self.writer('\n\nclass Operations:\n')
        for kind in kinds:
            self.writer('    %s = %s\n' % (kind, kind.title()))


def add_arguments(ap):
    ap.add_argument(
        'schema-name',
        help='The schema name to use in the imports. '
             'It must be in the form: `modname:symbol`. '
             'It may contain leading `.` to change the import '
             'statement to `from . import` using that as path. '
             'If `:symbol` is omitted, then `modname` is used.',
    )
    ap.add_argument(
        'operations.py', type=argparse.FileType('w'), nargs='?',
        help=('The output operations as Python file using '
              'sgqlc.operation. Defaults to the stdout'),
        default=sys.stdout,
    )
    ap.add_argument(
        'operation.gql',
        type=argparse.FileType('r'), nargs='*',
        help='The input GraphQL (DSL) with operations',
        default=[sys.stdin],
    )
    ap.add_argument(
        '--schema', type=argparse.FileType('r'),
        help=('The input schema as JSON file. '
              'Usually the output from introspection query. '
              'If given, the operations will be validated.'),
        default=None,
    )
    ap.add_argument(
        '--short-names', '-s',
        help='Use short selection names',
        default=False,
        action='store_true',
    )


def load_schema(in_file):
    if not in_file:
        return None

    schema = json.load(in_file)
    if not isinstance(schema, dict):
        raise SystemExit('schema must be a JSON object')

    if schema.get('types'):
        return schema
    elif schema.get('data', {}).get('__schema', None):
        return schema['data']['__schema']  # plain HTTP endpoint result
    elif schema.get('__schema'):
        return schema['__schema']  # introspection field
    else:
        raise SystemExit(
            'schema must be introspection object or query result')


def handle_command(parsed_args):
    args = vars(parsed_args)  # vars: operations.py and operation.gql
    schema = load_schema(args['schema'])
    schema_name = ParsedSchemaName.parse_schema_name(args['schema-name'])
    out_file = args['operations.py']
    in_files = args['operation.gql']
    short_names = args['short_names']

    operations_gql = [Source(f.read(), f.name) for f in in_files]

    gen = CodeGen(
        schema, schema_name, operations_gql,
        out_file.write, short_names,
    )
    gen.write()
    out_file.close()


def main():
    ap = argparse.ArgumentParser(
        description='Generate sgqlc operations using GraphQL (DSL)',
    )
    add_arguments(ap)
    handle_command(ap.parse_args())


if __name__ == '__main__':
    main()
