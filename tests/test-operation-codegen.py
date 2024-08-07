import os
from io import StringIO
from graphql import Source

from sgqlc.codegen.operation import CodeGen, load_schema, ParsedSchemaName


def test_operation_gen_nested_interface():
    result_buff = StringIO()
    test_schema_path = os.path.join(
        'tests', 'test-resources', 'operation-codegen', 'operation-test.json'
    )
    test_op_path = os.path.join(
        'tests', 'test-resources', 'operation-codegen', 'op-gen.gql'
    )
    schema_name = ParsedSchemaName.parse_schema_name('.schema')

    with open(test_op_path) as op_file, open(test_schema_path) as schema_file:
        operation_gql = [Source(op_file.read(), op_file.name)]
        schema = load_schema(schema_file)
        gen = CodeGen(
            schema,
            schema_name,
            operation_gql,
            result_buff.write,
            short_names=False,
        )
        gen.write()
        result_buff.close()
