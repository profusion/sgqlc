import sgqlc.types
import sgqlc.operation
import github_schema

_schema = github_schema
_schema_root = _schema.github_schema

__all__ = ('Operations',)


def query_list_issues():
    _op = sgqlc.operation.Operation(_schema_root.query_type, name='ListIssues', variables=dict(owner=sgqlc.types.Arg(sgqlc.types.non_null(_schema.String)), name=sgqlc.types.Arg(sgqlc.types.non_null(_schema.String)), desiredOrderBy=sgqlc.types.Arg(_schema.IssueOrder, default={'field': 'CREATED_AT', 'direction': 'ASC'}), filterStates=sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(_schema.IssueState)), default=('OPEN',))))
    _op_repository = _op.repository(owner=sgqlc.types.Variable('owner'), name=sgqlc.types.Variable('name'))
    _op_repository.__typename__()
    _op_repository_issues = _op_repository.issues(first=100, order_by=sgqlc.types.Variable('desiredOrderBy'), states=sgqlc.types.Variable('filterStates'))
    _op_repository_issues_nodes = _op_repository_issues.nodes()
    _op_repository_issues_nodes.number(__alias__='n')
    _op_repository_issues_nodes.title()
    _op_repository_issues_nodes__as__Node = _op_repository_issues_nodes.__as__(_schema.Node)
    _op_repository_issues_nodes__as__Node.id()
    _op_repository_issues_page_info = _op_repository_issues.page_info()
    _op_repository_issues_page_info.has_next_page()
    _op_repository_issues_page_info.end_cursor()
    _op_repository_rulesets = _op_repository.rulesets(last=None, include_parents=False)
    _op_repository_rulesets.total_count()
    return _op


class Query:
    list_issues = query_list_issues()


class Operations:
    query = Query
