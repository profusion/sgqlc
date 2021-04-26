#!/usr/bin/env python3

import argparse
import json
import os
import os.path
import sys
import re
import functools
import textwrap

from sgqlc.types import BaseItem

try:
    # graphql >= 3.0
    from graphql.language.ast import ValueNode as GraphQLASTValue
except ImportError:
    # graphql < 3.0 (ex: 2.2)
    from graphql.language.ast import Value as GraphQLASTValue
from graphql.language.parser import parse_value as parse_graphql_value
from graphql.language.visitor import Visitor, visit


# Use Null instead of None as Visitor.leave_* understands None as IDLE,
# which keeps the original node.
class Null:
    def __repr__(self):
        return 'None'


class JSONOutputVisitor(Visitor):
    def leave_IntValue(self, node, *args):
        return int(node.value)

    def leave_FloatValue(self, node, *args):
        return float(node.value)

    def leave_StringValue(self, node, *args):
        return node.value

    def leave_BooleanValue(self, node, *args):
        return node.value

    def leave_EnumValue(self, node, *args):
        return node.value

    def leave_ListValue(self, node, *args):
        return node.values

    def leave_ObjectValue(self, node, *args):
        return dict(node.fields)

    def leave_ObjectField(self, node, *args):
        return (node.name.value, node.value)

    def leave_NullValue(self, _node, *_args):
        return Null()

    leave_int_value = leave_IntValue
    leave_float_value = leave_FloatValue
    leave_string_value = leave_StringValue
    leave_boolean_value = leave_BooleanValue
    leave_enum_value = leave_EnumValue
    leave_list_value = leave_ListValue
    leave_object_value = leave_ObjectValue
    leave_object_field = leave_ObjectField
    leave_null_value = leave_NullValue


def parse_graphql_value_to_json(source):
    value = parse_graphql_value(source)
    v = visit(value, JSONOutputVisitor())
    if isinstance(v, GraphQLASTValue):
        v = v.value
    return v


paragraph_wrapper = textwrap.TextWrapper(
    width=70,
    expand_tabs=True,
    initial_indent='    ',
    subsequent_indent='    ',
)

list_wrapper = textwrap.TextWrapper(
    width=70,
    expand_tabs=True,
    initial_indent='    * ',
    subsequent_indent='      ',
)


def to_docstring(wrapped_text, level=1):
    if not wrapped_text:
        return ''
    prefix = '    ' * level
    if len(wrapped_text) == 1:
        suffix = ''
    else:
        suffix = '\n' + prefix

    wrapped_text[0] = wrapped_text[0].lstrip()
    return '%s\'\'\'%s%s\'\'\'\n' % (
        prefix,
        '\n'.join(wrapped_text),
        suffix,
    )


def graphql_type_to_str(t):
    kind = t['kind']
    if kind == 'NON_NULL':
        return '%s!' % (graphql_type_to_str(t['ofType']),)
    elif kind == 'LIST':
        return '[%s]' % (graphql_type_to_str(t['ofType']),)
    else:
        return t['name']


class CodeGen:
    def __init__(self, schema_name, schema, writer, docstrings):
        self.schema_name = schema_name
        self.schema = schema
        self.types = sorted(schema['types'], key=lambda x: x['name'])
        self.type_by_name = {t['name']: t for t in self.types}
        self.query_type = self.get_path('queryType', 'name')
        self.mutation_type = self.get_path('mutationType', 'name')
        self.subscription_type = self.get_path('subscriptionType', 'name')
        self.directives = schema.get('directives', [])
        self.analyze()
        self.writer = writer
        self.written_types = set()
        self.docstrings = docstrings

    def get_path(self, *path, fallback=None):
        d = self.schema
        path = list(path)
        while d and path:
            d = d.get(path.pop(0))

        if d is None:
            return fallback
        return d

    builtin_types = ('Int', 'Float', 'String', 'Boolean', 'ID')
    datetime_types = ('DateTime', 'Date', 'Time')
    relay_types = ('Node', 'PageInfo')

    def analyze(self):
        self.uses_datetime = False
        self.uses_relay = False
        for t in self.types:
            name = t['name']
            if name in self.datetime_types:
                self.uses_datetime = True
                if self.uses_relay:
                    break
            elif name in self.relay_types:
                self.uses_relay = True
                if self.uses_datetime:
                    break

    def write(self):
        self.write_header()
        self.write_types()
        self.write_entry_points()

    def write_banner(self, text):
        bar = '#' * 72
        self.writer('''
%(bar)s
# %(text)s
%(bar)s
''' % {
            'bar': bar,
            'text': text,
        })

    @staticmethod
    def has_iface(ifaces, name):
        for iface in ifaces:
            if name == iface['name']:
                return True
        return False

    # fields without interfaces first, then order the interface
    # implementor after the interface declaration
    def depend_cmp(a, b):
        a_ifaces = a['interfaces']
        b_ifaces = b['interfaces']
        if not a_ifaces and b_ifaces:
            return -1
        elif a_ifaces and not b_ifaces:
            return 1
        elif not a_ifaces and not b_ifaces:
            return 0

        has_iface = CodeGen.has_iface
        if len(a_ifaces) < len(b_ifaces):
            if has_iface(a_ifaces, b['name']):
                return 1
            elif has_iface(b_ifaces, a['name']):
                return -1
            else:
                return 0
        else:
            if has_iface(b_ifaces, a['name']):
                return -1
            elif has_iface(a_ifaces, b['name']):
                return 1
            else:
                return 0

    @staticmethod
    def get_depend_sort_key():
        return functools.cmp_to_key(CodeGen.depend_cmp)

    def write_types(self):
        mapper_basic = {
            'ENUM': self.write_type_enum,
            'SCALAR': self.write_type_scalar,
        }
        mapper_input_containers = {
            'INPUT_OBJECT': self.write_type_input_object,
        }
        mapper_output_containers = {
            'INTERFACE': self.write_type_interface,
            'OBJECT': self.write_type_object,
        }
        mapper_post = {
            'UNION': self.write_type_union,
        }

        self.write_banner('Scalars and Enumerations')
        todo = self.types
        remaining = []
        for t in todo:
            kind = t['kind']
            mapped = mapper_basic.get(kind)
            if mapped is None:
                remaining.append(t)
            else:
                mapped(t)

        self.write_banner('Input Objects')
        todo = remaining
        remaining = []
        for t in todo:
            kind = t['kind']
            mapped = mapper_input_containers.get(kind)
            if mapped is None:
                remaining.append(t)
            else:
                mapped(t)

        remaining.sort(key=self.get_depend_sort_key())
        self.write_banner('Output Objects and Interfaces')
        todo = remaining
        remaining = []
        for t in todo:
            kind = t['kind']
            mapped = mapper_output_containers.get(kind)
            if mapped is None:
                remaining.append(t)
            else:
                mapped(t)

        self.write_banner('Unions')
        todo = remaining
        remaining = []
        for t in todo:
            kind = t['kind']
            mapped = mapper_post.get(kind)
            if mapped is None:
                remaining.append(t)
            else:
                mapped(t)

        assert not remaining

    builtin_enum_names = ('__TypeKind', '__DirectiveLocation')

    def get_docstring(self, t):
        if not self.docstrings:
            return ''
        description = t.get('description')
        if not description:
            return ''
        return to_docstring(paragraph_wrapper.wrap(description))

    def get_enum_docstring(self, t):
        if not self.docstrings:
            return ''
        lines = []
        description = t.get('description')
        if description:
            lines.extend(paragraph_wrapper.wrap(description))
            lines.append('')

        lines.extend(paragraph_wrapper.wrap('Enumeration Choices:'))
        lines.append('')
        for c in t['enumValues']:
            d = c.get('description', '')
            if d:
                d = ': ' + d
            lines.extend(list_wrapper.wrap('`%s`%s' % (c['name'], d)))
        return to_docstring(lines)

    def write_field_docstring(self, field):
        if not self.docstrings:
            return
        lines = []
        description = field.get('description')
        if description:
            lines.extend(paragraph_wrapper.wrap(description))

        args = field.get('args')
        if args:
            if lines:
                lines.append('')
            lines.extend(paragraph_wrapper.wrap('Arguments:'))
            lines.append('')
            for a in args:
                n = BaseItem._to_python_name(a['name'])
                t = graphql_type_to_str(a['type'])
                d = a.get('description', '')
                if d:
                    d = ': ' + d
                defval = a.get('defaultValue')
                if defval is None:
                    defval = ''
                else:
                    defval = ' (default: `%s`)' % (defval,)
                lines.extend(list_wrapper.wrap(
                    '`%s` (`%s`)%s%s' % (n, t, d, defval)
                ))
        self.writer(to_docstring(lines))
        self.writer('\n')

    def write_type_enum(self, t):
        name = t['name']
        if name in self.builtin_enum_names:
            return
        self.writer('''\
class %(name)s(sgqlc.types.Enum):
%(docstrings)s\
    __schema__ = %(schema_name)s
    __choices__ = %(choices)r


''' % {
            'name': name,
            'schema_name': self.schema_name,
            'docstrings': self.get_enum_docstring(t),
            'choices': tuple(v['name'] for v in t['enumValues']),
        })
        self.written_types.add(name)

    def get_type_ref(self, t, siblings):
        kind = t['kind']
        if kind == 'NON_NULL':
            of_type = t['ofType']
            return 'sgqlc.types.non_null(%s)' % self.get_type_ref(
                of_type, siblings)
        elif kind == 'LIST':
            of_type = t['ofType']
            return 'sgqlc.types.list_of(%s)' % self.get_type_ref(
                of_type, siblings)

        name = t['name']
        if name in self.written_types and name not in siblings:
            return name
        else:
            return repr(name)

    def get_py_fields_and_siblings(self, own_fields):
        graphql_fields = tuple(field['name'] for field in own_fields)
        py_fields = tuple(
            BaseItem._to_python_name(f_name) for f_name in graphql_fields
        )
        return py_fields, set(graphql_fields)

    def write_field_input(self, field, siblings):
        name = field['name']
        tref = self.get_type_ref(field['type'], siblings)
        self.writer('''\
    %(py_name)s = sgqlc.types.Field(%(type)s, graphql_name=%(gql_name)r)
''' % {
            'py_name': BaseItem._to_python_name(name),
            'gql_name': name,
            'type': tref,
        })
        self.write_field_docstring(field)

    def write_arg(self, arg, siblings):
        name = arg['name']
        tref = self.get_type_ref(arg['type'], siblings)
        defval = arg.get('defaultValue')
        if defval:
            if defval.startswith('$'):
                defval = 'sgqlc.types.Variable(%r)' % defval[1:]
            else:
                defval = repr(parse_graphql_value_to_json(defval))

        self.writer('''\
        (%(py_name)r, sgqlc.types.Arg(%(type)s, graphql_name=%(gql_name)r, \
default=%(default)s)),
''' % {
            'py_name': BaseItem._to_python_name(name),
            'gql_name': name,
            'type': tref,
            'default': defval,
        })

    def write_field_output(self, field, siblings):
        name = field['name']
        tref = self.get_type_ref(field['type'], siblings)
        self.writer('''\
    %(py_name)s = sgqlc.types.Field(%(type)s, graphql_name=%(gql_name)r\
''' % {
            'py_name': BaseItem._to_python_name(name),
            'gql_name': name,
            'type': tref,
        })
        args = field['args']
        if args:
            self.writer(', args=sgqlc.types.ArgDict((\n')
            for a in args:
                self.write_arg(a, siblings)
            self.writer('))\n    ')

        self.writer(')\n')
        self.write_field_docstring(field)

    def write_type_container(self, t, bases, own_fields, write_field):
        name = t['name']
        py_fields, siblings = self.get_py_fields_and_siblings(own_fields)
        self.writer('''\
class %(name)s(%(bases)s):
%(docstrings)s\
    __schema__ = %(schema_name)s
    __field_names__ = %(field_names)s
''' % {
            'name': name,
            'bases': bases,
            'docstrings': self.get_docstring(t),
            'schema_name': self.schema_name,
            'field_names': py_fields,
        })
        for field in own_fields:
            write_field(field, siblings)
        self.writer('\n\n')
        self.written_types.add(name)

    def write_type_input_object(self, t):
        own_fields = t['inputFields']
        bases = 'sgqlc.types.Input'
        write_field = self.write_field_input
        self.write_type_container(t, bases, own_fields, write_field)

    def write_type_interface(self, t):
        own_fields = t['fields']
        bases = 'sgqlc.types.Interface'
        write_field = self.write_field_output
        self.write_type_container(t, bases, own_fields, write_field)

    builtin_object_names = (
        '__Schema',
        '__Type',
        '__Field',
        '__Directive',
        '__EnumValue',
        '__InputValue',
    )

    def write_type_object(self, t):
        name = t['name']
        if name in self.builtin_object_names:
            return
        if self.uses_relay and name.endswith('Connection'):
            bases = ['sgqlc.types.relay.Connection']
        else:
            bases = ['sgqlc.types.Type']

        inherited_fields = set()
        for iface in (t['interfaces'] or ()):
            iface_name = iface['name']
            assert iface_name in self.written_types, iface_name
            bases.append(iface_name)
            for field in self.type_by_name[iface_name]['fields']:
                inherited_fields.add(field['name'])

        own_fields = tuple(
            field
            for field in t['fields']
            if field['name'] not in inherited_fields
        )
        bases = ', '.join(bases)
        write_field = self.write_field_output
        self.write_type_container(t, bases, own_fields, write_field)

    def write_type_scalar(self, t):
        name = t['name']
        if name in self.builtin_types:
            self.writer('%(name)s = sgqlc.types.%(name)s' % t)
        elif name in self.datetime_types:
            self.writer('%(name)s = sgqlc.types.datetime.%(name)s' % t)
        else:
            self.writer('''\
class %(name)s(sgqlc.types.Scalar):
%(docstring)s\
    __schema__ = %(schema_name)s
''' % {
                'name': name,
                'docstring': self.get_docstring(t),
                'schema_name': self.schema_name,
            })
        self.writer('\n\n')
        self.written_types.add(name)

    def write_type_union(self, t):
        name = t['name']
        possible_types = t['possibleTypes']
        trailing_comma = ',' if len(possible_types) == 1 else ''
        self.writer('''\
class %(name)s(sgqlc.types.Union):
%(docstring)s\
    __schema__ = %(schema_name)s
    __types__ = (%(types)s%(trailing_comma)s)


''' % {
            'name': name,
            'docstring': self.get_docstring(t),
            'schema_name': self.schema_name,
            'types': ', '.join(v['name'] for v in possible_types),
            'trailing_comma': trailing_comma,
        })
        self.written_types.add(name)

    def write_header(self):
        self.writer('import sgqlc.types\n')
        self.write_datetime_import()
        self.write_relay_import()
        self.writer('\n\n%s = sgqlc.types.Schema()\n\n\n' % self.schema_name)
        self.write_relay_fixup()
        if self.docstrings:
            self.writer('__docformat__ = \'markdown\'\n\n')

    def write_datetime_import(self):
        if not self.uses_datetime:
            return
        self.writer('import sgqlc.types.datetime\n')

    def write_relay_import(self):
        if not self.uses_relay:
            return
        self.writer('import sgqlc.types.relay\n')

    def write_relay_fixup(self):
        if not self.uses_relay:
            return
        self.writer('''\
# Unexport Node/PageInfo, let schema re-declare them
%(schema_name)s -= sgqlc.types.relay.Node
%(schema_name)s -= sgqlc.types.relay.PageInfo


''' % {
            'schema_name': self.schema_name,
        })

    def write_entry_points(self):
        self.write_banner('Schema Entry Points')
        self.writer('''\
%(schema_name)s.query_type = %(query_type)s
%(schema_name)s.mutation_type = %(mutation_type)s
%(schema_name)s.subscription_type = %(subscription_type)s

''' % {
            'schema_name': self.schema_name,
            'query_type': self.query_type,
            'mutation_type': self.mutation_type,
            'subscription_type': self.subscription_type,
        })


def get_basename_noext(path):
    return os.path.splitext(os.path.basename(path))[0]


def gen_schema_name(out_file, in_fname):
    if out_file:
        if out_file.name != '<stdout>':
            return get_basename_noext(out_file.name)
        elif in_fname != '<stdin>':
            return get_basename_noext(in_fname)
        else:
            return 'generated_schema'
    else:
        if in_fname == '<stdin>':
            return 'generated_schema'
        else:
            return get_basename_noext(in_fname)


def cleanup_schema_name(schema_name):
    schema_name = re.sub('[^A-Za-z0-9_]+', '_', schema_name)
    schema_name = re.sub('(^_+|_+$)', '', schema_name)
    if re.match('^[0-9]', schema_name):
        schema_name = '_' + schema_name

    return schema_name


def gen_out_file(schema_name, in_fname):
    if in_fname == '<stdin>':
        return sys.stdout
    else:
        wd = os.path.dirname(in_fname)
        out_fname = os.path.join(wd, schema_name + '.py')
        sys.stdout.write('Writing to: %s\n' % (out_fname,))
        return open(out_fname, 'w')


def load_schema(in_file):
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


def add_arguments(ap):
    # Generic options to access the GraphQL API
    ap.add_argument('schema.json', type=argparse.FileType('r'), nargs='?',
                    help=('The input schema as JSON file. '
                          'Usually the output from introspection query.'),
                    default=sys.stdin)

    ap.add_argument('schema.py', type=argparse.FileType('w'), nargs='?',
                    help=('The output schema as Python file using '
                          'sgqlc.types. Defaults to the input schema name '
                          'with .py extension.'),
                    default=None)

    ap.add_argument('--schema-name', '-s',
                    help=('The schema name to use. '
                          'Defaults to output (or input) basename without '
                          'extension and invalid python identifiers replaced '
                          ' with "_".'),
                    default=None)
    ap.add_argument('--docstrings', '-d', action='store_true',
                    help=('Include schema descriptions in the generated file '
                          'as docstrings'),
                    default=False)


def handle_command(parsed_args):
    args = vars(parsed_args)  # vars: schema.json and schema.py
    in_file = args['schema.json']
    out_file = args['schema.py']

    in_fname = args['schema.json'].name

    schema_name = args['schema_name']
    if not schema_name:
        schema_name = gen_schema_name(out_file, in_fname)

    schema_name = cleanup_schema_name(schema_name)

    if not out_file:
        out_file = gen_out_file(schema_name, in_fname)

    schema = load_schema(in_file)

    docstrings = args['docstrings'] or False

    gen = CodeGen(schema_name, schema, out_file.write, docstrings)
    gen.write()
    out_file.close()


def main():
    ap = argparse.ArgumentParser(
        description='Generate sgqlc types using GraphQL introspection data',
    )
    add_arguments(ap)
    handle_command(ap.parse_args())


if __name__ == '__main__':
    main()
