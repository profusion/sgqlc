Example: Simple GraphQL Client
------------------------

Usage:

```bash
pipenv install -d
pipenv shell
export GH_TOKEN=<your github API token>

cd examples/basic
python3 01_http_endpoint.py $GH_TOKEN profusion/sgqlc
```

The `01_http_endpoint.py` example shows how you can query a GraphQL endpoint with a text query, while
specifying variables and HTTP headers. The result comes back as a dictionary.

To generate the query dynamically, and have the results come back as native objects, look at the
`02_schema_types.py` example. It shows how you can declare classes locally to mirror the types that are
defined on the graphql schema that you'd like to work with. Those 'type' classes can be used
to have *sgqlc* generate queries dynamically, and interpret the results. E.g.

```bash
python3 02_schema_types.py $GH_TOKEN profusion/sgqlc
```
