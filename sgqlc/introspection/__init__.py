'''
Introspection
=============

Provides the standard GraphQL Introspection Query, same as
https://github.com/graphql/graphql-js/blob/master/src/utilities/introspectionQuery.js
however allows to choose whether to include descriptions and
deprecated fields.

Downloading schema.json
-----------------------

Usually services provide a ``schema.json`` file with the introspection results
or offer a development server where the introspection query can be executed
and saved as JSON:

.. code-block:: shell

    python3 \\
        -m sgqlc.introspection \\
        --exclude-deprecated \\
        -H "Authorization: bearer ${TOKEN}" \\
        https://server.com/graphql \\
        schema.json

If the descriptions are not needed, then they can be excluded (saves
bandwith and space):

.. code-block:: shell

    python3 \\
        -m sgqlc.introspection \\
        --exclude-deprecated \\
        --exclude-description \\
        -H "Authorization: bearer ${TOKEN}" \\
        https://server.com/graphql \\
        schema.json


:license: ISC
'''

__docformat__ = 'reStructuredText en'

# Introspection query from Facebook's GraphQL Project:
# https://github.com/graphql/graphql-js/blob/master/
# src/utilities/introspectionQuery.js
#
# tweaked to include Arguments:
#  - includeDescription: add documentation (description)
#  - includeDeprecated: if deprecated fields should be included
query = '''
query IntrospectionQuery(
  $includeDescription: Boolean!,
  $includeDeprecated: Boolean!,
) {
  __schema {
    queryType { name }
    mutationType { name }
    subscriptionType { name }
    types {
      ...FullType
    }
    directives {
      name
      description @include(if: $includeDescription)
      locations
      args {
        ...InputValue
      }
    }
  }
}

fragment FullType on __Type {
  kind
  name
  description @include(if: $includeDescription)
  fields(includeDeprecated: $includeDeprecated) {
    name
    description @include(if: $includeDescription)
    args {
      ...InputValue
    }
    type {
      ...TypeRef
    }
    isDeprecated @include(if: $includeDeprecated)
    deprecationReason @include(if: $includeDeprecated)
  }
  inputFields {
    ...InputValue
  }
  interfaces {
    ...TypeRef
  }
  enumValues(includeDeprecated: $includeDeprecated) {
    name
    description @include(if: $includeDescription)
    isDeprecated @include(if: $includeDeprecated)
    deprecationReason @include(if: $includeDeprecated)
  }
  possibleTypes {
    ...TypeRef
  }
}

fragment InputValue on __InputValue {
  name
  description @include(if: $includeDescription)
  type { ...TypeRef }
  defaultValue
}

fragment TypeRef on __Type {
  kind
  name
  ofType {
    kind
    name
    ofType {
      kind
      name
      ofType {
        kind
        name
        ofType {
          kind
          name
          ofType {
            kind
            name
            ofType {
              kind
              name
              ofType {
                kind
                name
              }
            }
          }
        }
      }
    }
  }
}
'''


def variables(include_description=True, include_deprecated=True):
    '''Return variables to be used with ``IntrospectionQuery`` GraphQL
    operation.

    :param include_description: If field and type descriptions
      (documentation) should be included in the query.
    :type include_description: bool

    :param include_deprecated: If deprecated fields and enumeration
      values should be included. If so, then two extra fields will be
      added: ``isDeprecated: Boolean`` and ``deprecationReason: String``.
    :type include_deprecated: bool

    :return: dict with GraphQL variables.
    :rtype: dict
    '''
    return {
        'includeDescription': include_description,
        'includeDeprecated': include_deprecated,
    }
