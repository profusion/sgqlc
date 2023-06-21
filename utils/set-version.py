#!/usr/bin/env python3

import sys
import re

try:
    version = sys.argv[1]
except IndexError:
    raise SystemExit('must provide version')


version_regexp = '(?P<version>\\d+(?:\\.\\d+(?:\\.\\d+)?)?)'


def patch(file, replacement):
    with open(file, 'r') as input_file:
        data = input_file.read()
        pattern = replacement.replace('@VERSION@', version_regexp)

        # repl = replacement.replace('@VERSION@', version)
        def repl(m):
            match_str = m.group(0)
            match_start, match_end = m.span()
            version_start, version_end = m.span('version')
            if version_start < 0:
                raise SystemExit(
                    'could not match version in replacement: %r' % (pattern,)
                )
            prefix_size = version_start - match_start
            suffix_size = match_end - version_end
            prefix = match_str[:prefix_size]
            suffix = match_str[-suffix_size:]
            return prefix + version + suffix

        replaced = re.sub(pattern, repl, data, flags=re.MULTILINE)
        if data == replaced:
            print('{}: up to date'.format(file))
        else:
            with open(file, 'w') as output_file:
                output_file.write(replaced)
                print(
                    '{}: updated {!r} to version {}'.format(
                        file, replacement, version
                    )
                )


replacements = (
    ('pyproject.toml', '^\\s*version\\s*=\\s*[\'"]@VERSION@[\'"]'),
    ('sgqlc/__init__.py', '^__version__\\s*=\\s*[\'"]@VERSION@[\'"]'),
    ('doc/source/conf.py', '^version\\s*=\\s*[\'"]@VERSION@[\'"]'),
    ('doc/source/conf.py', '^release\\s*=\\s*[\'"]@VERSION@[\'"]'),
)


for file, regexp in replacements:
    patch(file, regexp)
