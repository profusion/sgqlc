'''
GraphQL Types for :mod:`datetime`
=================================

Maps:

 - :class:`datetime.time` to GraphQL :class:`Time`
 - :class:`datetime.date` to GraphQL :class:`Date`
 - :class:`datetime.datetime` to GraphQL :class:`DateTime`

You may either explicitly use this module classes or :mod:`datetime`,
as they will be automatically recognized by the framework.

Conversions assume ISO 8601 encoding.

Examples
--------

>>> from sgqlc.types import Type
>>> class MyDateTimeType(Type):
...     time1 = datetime.time
...     time2 = Time
...     date1 = datetime.date
...     date2 = Date
...     datetime1 = datetime.datetime
...     datetime2 = DateTime
...
>>> MyDateTimeType # or repr() to print out GraphQL
type MyDateTimeType {
  time1: Time
  time2: Time
  date1: Date
  date2: Date
  datetime1: DateTime
  datetime2: DateTime
}
>>> json_data = {
...     'time1': '12:34:56',
...     'time2': '12:34:56-03:00', # set timezone GMT-3h
...     'date1': '2018-01-02',
...     'date2': '20180102', # compact form is accepted
...     'datetime1': '2018-01-02T12:34:56Z', # Z = GMT/UTC
...     'datetime2': '20180102T123456-0300', # compact form is accepted
... }
>>> obj = MyDateTimeType(json_data)
>>> for field_name in obj: # doctest: +ELLIPSIS
...     print(field_name, repr(obj[field_name]))
time1 datetime.time(12, 34, 56)
time2 datetime.time(12, 34, 56, tzinfo=...(...-1, ...75600)))
date1 datetime.date(2018, 1, 2)
date2 datetime.date(2018, 1, 2)
datetime1 datetime.datetime(2018, 1, 2, 12, 34, 56, tzinfo=....utc)
datetime2 datetime.datetime(2018, 1, 2, 12, 34, 56, tzinfo=...75600)))

Pre-converted types are allowed:

>>> json_data = { 'time1': datetime.time(12, 34, 56) }
>>> obj = MyDateTimeType(json_data)
>>> obj.time1
datetime.time(12, 34, 56)

However, invalid encoded strings are not:

>>> json_data = { 'time1': '12-3' }
>>> obj = MyDateTimeType(json_data)  # doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
   ...
ValueError: MyDateTimeType selection 'time1': ...
>>> json_data = { 'date1': '12-3' }
>>> obj = MyDateTimeType(json_data)  # doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
   ...
ValueError: MyDateTimeType selection 'date1': ...
>>> json_data = { 'datetime1': '2018-01-02X12-34-56Z' }
>>> obj = MyDateTimeType(json_data)  # doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
   ...
ValueError: MyDateTimeType selection 'datetime1': ...

:license: ISC
'''

__docformat__ = 'reStructuredText en'

__all__ = ('Time', 'Date', 'DateTime')

import datetime
import re

from . import Scalar, map_python_to_graphql


class Time(Scalar):
    '''Time encoded as string using ISO8601 (HH:MM:SS[.mmm][+/-HH:MM])

    While not a standard GraphQL type, it's often used, so expose to
    make life simpler.

    >>> Time('12:34:56') # naive, no timezone
    datetime.time(12, 34, 56)
    >>> Time('12:34:56Z') # Z = GMT/UTC
    datetime.time(12, 34, 56, tzinfo=datetime.timezone.utc)
    >>> Time('12:34:56-05:30') # doctest: +ELLIPSIS
    datetime.time(12, 34, 56, tzinfo=...(...-1, ...70200)))
    >>> Time('12:34:56+05:30') # doctest: +ELLIPSIS
    datetime.time(12, 34, 56, tzinfo=...(...19800)))
    >>> Time('123456') # compact form
    datetime.time(12, 34, 56)
    >>> Time('123456Z') # compact form, GMT/UTC
    datetime.time(12, 34, 56, tzinfo=datetime.timezone.utc)
    >>> Time('123456-0530') # doctest: +ELLIPSIS
    datetime.time(12, 34, 56, tzinfo=...(...-1, ...70200)))
    >>> Time('123456+0530') # doctest: +ELLIPSIS
    datetime.time(12, 34, 56, tzinfo=...(...19800)))

    Pre-converted values are allowed:

    >>> Time(datetime.time(12, 34, 56))
    datetime.time(12, 34, 56)

    It can also serialize to JSON:

    >>> Time.__to_json_value__(datetime.time(12, 34, 56))
    '12:34:56'
    >>> tzinfo = datetime.timezone.utc
    >>> Time.__to_json_value__(datetime.time(12, 34, 56, 0, tzinfo))
    '12:34:56+00:00'
    >>> Time.__to_json_value__('12:34:56')
    '12:34:56'
    >>> Time.__to_json_value__(None)

    '''

    _re_parse = re.compile(
        r'^(?P<H>\d{2}):?(?P<M>\d{2}):?(?P<S>\d{2})(?P<MS>|[.]\d+)'
        r'(?P<TZ>|Z|(?P<TZH>[+-]\d{2}):?(?P<TZM>\d{2}))$')

    @classmethod
    def converter(cls, s):
        if isinstance(s, datetime.time):
            return s
        m = cls._re_parse.match(s)
        if not m:
            raise ValueError('not in ISO 8601 format HH:MM:SS: %s' % s)

        hour = int(m.group('H'))
        minute = int(m.group('M'))
        second = int(m.group('S'))
        microsecond = int(m.group('MS')[1:] or 0)
        tzinfo = None
        if m.group('TZ') == 'Z':
            tzinfo = datetime.timezone.utc
        elif m.group('TZ'):
            d = datetime.timedelta(
                hours=int(m.group('TZH')),
                minutes=int(m.group('TZM')),
            )
            tzinfo = datetime.timezone(d)

        return datetime.time(hour, minute, second, microsecond, tzinfo)

    @classmethod
    def __to_json_value__(cls, value):
        if value is None:
            return None
        if isinstance(value, str):
            return value
        return value.isoformat()


class Date(Scalar):
    '''Date encoded as string using ISO8601 (YYYY-MM-SS)

    While not a standard GraphQL type, it's often used, so expose to
    make life simpler.

    >>> Date('2018-01-02')
    datetime.date(2018, 1, 2)
    >>> Date('20180102') # compact form
    datetime.date(2018, 1, 2)

    Pre-converted values are allowed:

    >>> Date(datetime.date(2018, 1, 2))
    datetime.date(2018, 1, 2)

    It can also serialize to JSON:

    >>> Date.__to_json_value__(datetime.date(2018, 1, 2))
    '2018-01-02'
    >>> Date.__to_json_value__('2018-01-02')
    '2018-01-02'
    >>> Date.__to_json_value__(None)

    '''

    _re_parse = re.compile(r'^(?P<Y>\d{4})-?(?P<m>\d{2})-?(?P<d>\d{2})$')

    @classmethod
    def converter(cls, s):
        if isinstance(s, datetime.date):
            return s
        m = cls._re_parse.match(s)
        if not m:
            raise ValueError('not in ISO 8601 format YYYY-MM-DD: %s' % s)

        year = int(m.group('Y'))
        month = int(m.group('m'))
        day = int(m.group('d'))
        return datetime.date(year, month, day)

    @classmethod
    def __to_json_value__(cls, value):
        if value is None:
            return None
        if isinstance(value, str):
            return value
        return value.isoformat()


class DateTime(Scalar):
    '''Date and Time encoded as string using ISO8601
    (YYYY-mm-ddTHH:MM:SS[.mmm][+/-HH:MM])

    While not a standard GraphQL type, it's often used, so expose to
    make life simpler.

    >>> DateTime('2018-01-02T12:34:56') # naive, no timezone
    datetime.datetime(2018, 1, 2, 12, 34, 56)
    >>> DateTime('2018-01-02T12:34:56Z') # Z = GMT/UTC
    datetime.datetime(2018, 1, 2, 12, 34, 56, tzinfo=datetime.timezone.utc)
    >>> DateTime('2018-01-02T12:34:56-05:30') # doctest: +ELLIPSIS
    datetime.datetime(2018, 1, 2, 12, 34, 56, tzinfo=..., ...70200)))
    >>> DateTime('2018-01-02T12:34:56+05:30') # doctest: +ELLIPSIS
    datetime.datetime(2018, 1, 2, 12, 34, 56, tzinfo=...(...19800)))
    >>> DateTime('20180102T123456') # compact form
    datetime.datetime(2018, 1, 2, 12, 34, 56)
    >>> DateTime('20180102T123456Z') # compact form, GMT/UTC
    datetime.datetime(2018, 1, 2, 12, 34, 56, tzinfo=datetime.timezone.utc)
    >>> DateTime('20180102T123456-0530') # doctest: +ELLIPSIS
    datetime.datetime(2018, 1, 2, 12, 34, 56, tzinfo=..., ...70200)))
    >>> DateTime('20180102T123456+0530') # doctest: +ELLIPSIS
    datetime.datetime(2018, 1, 2, 12, 34, 56, tzinfo=...(...19800)))

    Pre-converted values are allowed:

    >>> DateTime(datetime.datetime(2018, 1, 2, 12, 34, 56))
    datetime.datetime(2018, 1, 2, 12, 34, 56)

    It can also serialize to JSON:

    >>> dt = datetime.datetime(2018, 1, 2, 12, 34, 56)
    >>> DateTime.__to_json_value__(dt)
    '2018-01-02T12:34:56'
    >>> DateTime.__to_json_value__('2018-01-02T12:34:56')
    '2018-01-02T12:34:56'
    >>> tzinfo = datetime.timezone.utc
    >>> DateTime.__to_json_value__(dt.replace(tzinfo=tzinfo))
    '2018-01-02T12:34:56+00:00'
    >>> DateTime.__to_json_value__(None)

    '''

    _re_parse = re.compile(
        r'^(?P<Y>\d{4})-?(?P<m>\d{2})-?(?P<d>\d{2})T'
        r'(?P<H>\d{2}):?(?P<M>\d{2}):?(?P<S>\d{2})(?P<MS>|[.]\d+)'
        r'(?P<TZ>|Z|(?P<TZH>[+-]\d{2}):?(?P<TZM>\d{2}))$')

    @classmethod
    def converter(cls, s):
        if isinstance(s, datetime.datetime):
            return s
        m = cls._re_parse.match(s)
        if not m:
            raise ValueError('not in ISO 8601 format YYYY-MM-DDTHH:MM:SS: %s'
                             % s)

        year = int(m.group('Y'))
        month = int(m.group('m'))
        day = int(m.group('d'))
        hour = int(m.group('H'))
        minute = int(m.group('M'))
        second = int(m.group('S'))
        microsecond = int(m.group('MS')[1:] or 0)
        tzinfo = None
        if m.group('TZ') == 'Z':
            tzinfo = datetime.timezone.utc
        elif m.group('TZ'):
            d = datetime.timedelta(
                hours=int(m.group('TZH')),
                minutes=int(m.group('TZM')),
            )
            tzinfo = datetime.timezone(d)

        return datetime.datetime(year, month, day,
                                 hour, minute, second, microsecond, tzinfo)

    @classmethod
    def __to_json_value__(cls, value):
        if value is None:
            return None
        if isinstance(value, str):
            return value
        return value.isoformat()


map_python_to_graphql.update({
    datetime.time: Time,
    datetime.date: Date,
    datetime.datetime: DateTime,
})
