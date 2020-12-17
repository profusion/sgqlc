import sgqlc.types
import sgqlc.operation
import github_schema

__all__ = ('Operations',)


def query_list_issues():
    _op = sgqlc.operation.Operation(github_schema.github_schema.query_type, name='ListIssues', variables=dict(owner=sgqlc.types.Arg(sgqlc.types.non_null(github_schema.github_schema.String)), name=sgqlc.types.Arg(sgqlc.types.non_null(github_schema.github_schema.String))))
    _op_repository = _op.repository(owner=sgqlc.types.Variable('owner'), name=sgqlc.types.Variable('name'))
    _op_repository_issues = _op_repository.issues(first=100)
    _op_repository_issues_nodes = _op_repository_issues.nodes()
    _op_repository_issues_nodes.number()
    _op_repository_issues_nodes.title()
    _op_repository_issues_page_info = _op_repository_issues.page_info()
    _op_repository_issues_page_info.has_next_page()
    _op_repository_issues_page_info.end_cursor()
    return _op


class Query:
    list_issues = query_list_issues()


class Operations:
    query = Query
