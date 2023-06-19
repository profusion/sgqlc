'''
GraphQL Types for :mod:`uuid`
=================================

Maps:

 - :class:`uuid.UUID` to GraphQL :class:`UUID`

You may either explicitly use this module class: UUID or :mod:`uuid`,
as they will be automatically recognized by the framework.

Examples
--------

With both module and class :

>>> from sgqlc.types import Type
>>> from sgqlc.types.uuid import UUID
>>> import uuid
>>> class UUIDTestType(Type):
...     uuid1=UUID
...     uuid2=uuid.UUID
...
>>> UUIDTestType
type UUIDTestType {
  uuid1: UUID
  uuid2: UUID
}
>>> nested_json_data = {}
>>> nested_json_data['uuid1'] = '94fda4fb-d574-470b-82e2-0f4ec2a2db20'
>>> nested_json_data['uuid2'] = '94fda4fb-d574-470b-82e2-0f4ec2a2db21'
>>> obj = UUIDTestType(nested_json_data)
>>> for field in obj:
...     print(field, repr(obj[field]))
...
uuid1 UUID('94fda4fb-d574-470b-82e2-0f4ec2a2db20')
uuid2 UUID('94fda4fb-d574-470b-82e2-0f4ec2a2db21')


With valid uuid value:

>>> class MyUuidType(Type):
...     uuid = UUID
...
>>> MyUuidType # or repr() to print out GraphQL
type MyUuidType {
  uuid: UUID
}
>>> json_data = {'uuid': '94fda4fb-d574-470b-82e2-0f4ec2a2db20'}
>>> obj = MyUuidType(json_data)
>>> obj.uuid
UUID('94fda4fb-d574-470b-82e2-0f4ec2a2db20')

Pre-converted type is allowed:

>>> json_data = {'uuid': UUID('94fda4fb-d574-470b-82e2-0f4ec2a2db20')}
>>> obj = MyUuidType(json_data) # doctest: +ELLIPSIS
>>> obj.uuid
UUID('94fda4fb-d574-470b-82e2-0f4ec2a2db20')

>>> UUID('94fda4fb-d574-470b-82e2-0f4ec2a2db20') # doctest: +ELLIPSIS
UUID('94fda4fb-d574-470b-82e2-0f4ec2a2db20')

With input serialize to JSON:
>>> UUID.__to_json_value__('94fda4fb-d574-470b-82e2-0f4ec2a2db20')
'94fda4fb-d574-470b-82e2-0f4ec2a2db20'
>>> UUID.__to_json_value__(UUID('94fda4fb-d574-470b-82e2-0f4ec2a2db20'))
'94fda4fb-d574-470b-82e2-0f4ec2a2db20'
>>> UUID.__to_json_value__(None) # doctest: +ELLIPSIS

Invalid encoded strings are not:

>>> json_data = {'uuid': 'test 123'}
>>> obj = MyUuidType(json_data) # doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
   ...
ValueError: MyUuidType selection 'uuid': ...

>>> json_data = {'uuid': 123}
>>> obj = MyUuidType(json_data) # doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
   ...
ValueError: MyUuidType selection 'uuid': ...


With null input value:

>>> json_data = {'uuid': None}
>>> obj = MyUuidType(json_data)
>>> obj.uuid

All types of UUID supported:

>>> UUID('5e0d844c-b5bf-11ed-afa1-0242ac120002') # with UUID1
UUID('5e0d844c-b5bf-11ed-afa1-0242ac120002')
>>> UUID('000003e8-b5bf-21ed-9300-325096b39f47') # with UUID2
UUID('000003e8-b5bf-21ed-9300-325096b39f47')
>>> UUID('d5946b2b-447f-3fdf-8366-6c747863484a') # with UUID3
UUID('d5946b2b-447f-3fdf-8366-6c747863484a')
>>> UUID('54f4530b-3052-47b3-9231-b00f8d423448') # with UUID4
UUID('54f4530b-3052-47b3-9231-b00f8d423448')
>>> UUID('5a54a66f-bd21-559f-92fe-7ede767ed4b3') # with UUID5
UUID('5a54a66f-bd21-559f-92fe-7ede767ed4b3')

'''

__docformat__ = 'reStructuredText en'

__all__ = ('UUID',)

import uuid
import re

from . import Scalar, map_python_to_graphql


class UUID(Scalar):
    _re_parse = re.compile(
        r'(^[0-9a-f]{8}-[0-9a-f]{4}-[0-5][0-9a-f]{3})'
        r'-[089ab][0-9a-f]{3}-[0-9a-f]{12}$'
    )

    @classmethod
    def converter(cls, s):
        if isinstance(s, uuid.UUID):
            return s
        m = cls._re_parse.match(s)
        if not m:
            raise ValueError('not valid UUID format %s' % s)

        return uuid.UUID(s)

    @classmethod
    def __to_json_value__(cls, value):
        if value is None:
            return None
        if isinstance(value, str):
            return value
        return str(value)


map_python_to_graphql.update({uuid.UUID: UUID})
