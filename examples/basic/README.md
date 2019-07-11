Example: Simple GraphQL Client
------------------------


Usage:

```
pipenv install -d
pipenv shell
export GH_TOKEN=<your github API token>

python examples/basic/http-endpoint.py $GH_TOKEN profusion/sgqlc
```

The `http-endpoint.py` example shows how you can query a GraphQL endpoint with a text query, while
specifying variables and HTTP headers. The result comes back as a dictionary.

To generate the query dynamically, and have the results come back as native objects, look at the
`types.py` example. It shows how you can declare classes locally to mirror the types that are
defined on the graphql schema that you'd like to work with. Those 'type' classes can be used
to have *sgqlc* generate queries dynamically, and interpret the results. E.g.

```
python examples/basic/types.py $GH_TOKEN profusion/sgqlc
```
