#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os.path
from setuptools import setup, find_packages

name = 'sgqlc'
version = 1
release = 1


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()


setup(
    name=name,
    version=version,
    description='Simple GraphQL Client',
    long_description=read('README.rst'),
    author='Gustavo Sverzut Barbieri',
    author_email='barbieri@profusion.mobi',
    url='http://github.com/profusion/sgqlc',
    license='ISCL',
    python_requires='>=3.6',
    requires=[],
    extras_require={
        'sphinx': ['sphinx'],
    },
    zip_safe=True,
    keywords='graphql client http endpoint',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
    platforms='any',
    scripts=[
        'bin/sgqlc-codegen',
    ],
    packages=find_packages(exclude=('doc', 'examples', 'utils', 'tests')),
    test_suite='nose.collector',
    tests_require=['nose', 'coverage'],
    command_options={
        'build_sphinx': {
            'project': ('setup.py', name),
            'version': ('setup.py', str(version)),
            'release': ('setup.py', str(release)),
        }
    },
)
