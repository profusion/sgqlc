'''
sgqlc - Simple GraphQL Client
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

GraphQL Types for :mod:`datetime`
=================================

Maps:

 - :class:`datetime.time` to GraphQL :class:`Time`
 - :class:`datetime.date` to GraphQL :class:`Date`
 - :class:`datetime.datetime` to GraphQL :class:`DateTime`

You may either explicitly use this module classes or :mod:`datetime`,
as they will be automatically recognized by the framework.

Conversions assume ISO 8601 encoding.

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

        hour = int(m['H'])
        minute = int(m['M'])
        second = int(m['S'])
        microsecond = int(m['MS'][1:] or 0)
        tzinfo = None
        if m['TZ'] == 'Z':
            tzinfo = datetime.timezone.utc
        elif m['TZ']:
            d = datetime.timedelta(hours=int(m['TZH']), minutes=int(m['TZM']))
            tzinfo = datetime.timezone(d)

        return datetime.time(hour, minute, second, microsecond, tzinfo)

    @classmethod
    def __to_json_value__(cls, value):
        return None if value is None else value.isoformat()


class Date(Scalar):
    '''Date encoded as string using ISO8601 (YYYY-MM-SS)

    While not a standard GraphQL type, it's often used, so expose to
    make life simpler.
    '''

    _re_parse = re.compile(r'^(?P<Y>\d{4})-?(?P<m>\d{2})-?(?P<d>\d{2})$')

    @classmethod
    def converter(cls, s):
        if isinstance(s, datetime.date):
            return s
        m = cls._re_parse.match(s)
        if not m:
            raise ValueError('not in ISO 8601 format YYYY-MM-DD: %s' % s)

        year = int(m['Y'])
        month = int(m['m'])
        day = int(m['d'])
        return datetime.date(year, month, day)

    @classmethod
    def __to_json_value__(cls, value):
        return None if value is None else value.isoformat()


class DateTime(Scalar):
    '''Date and Time encoded as string using ISO8601
    (YYYY-mm-ddTHH:MM:SS[.mmm][+/-HH:MM])

    While not a standard GraphQL type, it's often used, so expose to
    make life simpler.
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

        year = int(m['Y'])
        month = int(m['m'])
        day = int(m['d'])
        hour = int(m['H'])
        minute = int(m['M'])
        second = int(m['S'])
        microsecond = int(m['MS'][1:] or 0)
        tzinfo = None
        if m['TZ'] == 'Z':
            tzinfo = datetime.timezone.utc
        elif m['TZ']:
            d = datetime.timedelta(hours=int(m['TZH']), minutes=int(m['TZM']))
            tzinfo = datetime.timezone(d)

        return datetime.datetime(year, month, day,
                                 hour, minute, second, microsecond, tzinfo)

    @classmethod
    def __to_json_value__(cls, value):
        return None if value is None else value.isoformat()


map_python_to_graphql.update({
    datetime.time: Time,
    datetime.date: Date,
    datetime.datetime: DateTime,
})
