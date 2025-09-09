from io import StringIO
from graphql import Source

from sgqlc.codegen.operation import CodeGen, load_schema, ParsedSchemaName


NESTED_INTERFACE_QUERY = """
query TestQuery {
    foo {
        ... on Bar {
            barField
        }
    }
}
"""

NESTED_INTERFACE_SCHEMA = """
{
  "__schema": {
    "queryType": {
      "name": "Query"
    },
    "mutationType": null,
    "subscriptionType": null,
    "types": [
      {
        "kind": "OBJECT",
        "name": "Query",
        "description": null,
        "fields": [
          {
            "name": "foo",
            "description": null,
            "args": [],
            "type": {
              "kind": "INTERFACE",
              "name": "Foo",
              "ofType": null
            },
            "isDeprecated": false,
            "deprecationReason": null
          }
        ],
        "inputFields": null,
        "interfaces": [],
        "enumValues": null,
        "possibleTypes": null
      },
      {
        "kind": "INTERFACE",
        "name": "Foo",
        "description": null,
        "fields": [
          {
            "name": "fooField",
            "description": null,
            "args": [],
            "type": {
              "kind": "NON_NULL",
              "name": null,
              "ofType": {
                "kind": "SCALAR",
                "name": "String",
                "ofType": null
              }
            },
            "isDeprecated": false,
            "deprecationReason": null
          }
        ],
        "inputFields": null,
        "interfaces": [],
        "enumValues": null,
        "possibleTypes": [
          {
            "kind": "OBJECT",
            "name": "Baz",
            "ofType": null
          }
        ]
      },
      {
        "kind": "SCALAR",
        "name": "String",
        "description": "The `String` scalar type represents textual data",
        "fields": null,
        "inputFields": null,
        "interfaces": null,
        "enumValues": null,
        "possibleTypes": null
      },
      {
        "kind": "INTERFACE",
        "name": "Bar",
        "description": null,
        "fields": [
          {
            "name": "fooField",
            "description": null,
            "args": [],
            "type": {
              "kind": "NON_NULL",
              "name": null,
              "ofType": {
                "kind": "SCALAR",
                "name": "String",
                "ofType": null
              }
            },
            "isDeprecated": false,
            "deprecationReason": null
          },
          {
            "name": "barField",
            "description": null,
            "args": [],
            "type": {
              "kind": "NON_NULL",
              "name": null,
              "ofType": {
                "kind": "SCALAR",
                "name": "String",
                "ofType": null
              }
            },
            "isDeprecated": false,
            "deprecationReason": null
          }
        ],
        "inputFields": null,
        "interfaces": [
          {
            "kind": "INTERFACE",
            "name": "Foo",
            "ofType": null
          }
        ],
        "enumValues": null,
        "possibleTypes": [
          {
            "kind": "OBJECT",
            "name": "Baz",
            "ofType": null
          }
        ]
      },
      {
        "kind": "OBJECT",
        "name": "Baz",
        "description": null,
        "fields": [
          {
            "name": "barField",
            "description": null,
            "args": [],
            "type": {
              "kind": "NON_NULL",
              "name": null,
              "ofType": {
                "kind": "SCALAR",
                "name": "String",
                "ofType": null
              }
            },
            "isDeprecated": false,
            "deprecationReason": null
          },
          {
            "name": "fooField",
            "description": null,
            "args": [],
            "type": {
              "kind": "NON_NULL",
              "name": null,
              "ofType": {
                "kind": "SCALAR",
                "name": "String",
                "ofType": null
              }
            },
            "isDeprecated": false,
            "deprecationReason": null
          }
        ],
        "inputFields": null,
        "interfaces": [
          {
            "kind": "INTERFACE",
            "name": "Bar",
            "ofType": null
          },
          {
            "kind": "INTERFACE",
            "name": "Foo",
            "ofType": null
          }
        ],
        "enumValues": null,
        "possibleTypes": null
      }
    ]
  }
}
"""


def test_operation_gen_nested_interface():
    expected_generated_query = """def query_test_query():
    _op = sgqlc.operation.Operation(_schema_root.query_type, name='TestQuery')
    _op_foo = _op.foo()
    _op_foo__as__Bar = _op_foo.__as__(_schema.Bar)
    _op_foo__as__Bar.bar_field()
    return _op"""
    result_buff = StringIO()
    schema_name = ParsedSchemaName.parse_schema_name('.schema')

    with StringIO(NESTED_INTERFACE_QUERY) as op_file, StringIO(
        NESTED_INTERFACE_SCHEMA
    ) as schema_file:
        operation_gql = [Source(op_file.read(), 'op-gen.gql')]
        schema = load_schema(schema_file)
        gen = CodeGen(
            schema,
            schema_name,
            operation_gql,
            result_buff.write,
            short_names=False,
        )
        gen.write()
        generated_operations = result_buff.getvalue()
        result_buff.close()
        assert expected_generated_query in generated_operations
