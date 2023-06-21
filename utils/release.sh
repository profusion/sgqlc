#!/bin/bash

SETUP_VERSION=`poetry version --short`
MOD_VERSION=`PYTHONPATH='.' python3 -c 'import sgqlc; print(sgqlc.__version__)'`
if [ $SETUP_VERSION != $MOD_VERSION ]; then
  echo "update both pyproject.toml and sgqlc/__init__.py so versions match" >&2
  exit 1
fi
DOC_VERSION=`PYTHONPATH='.' python3 -c 'import doc.source.conf; print(doc.source.conf.version)'`
if [ $SETUP_VERSION != $DOC_VERSION ]; then
  echo "update both pyproject.toml and doc/source/conf.py so versions match" >&2
  exit 1
fi

rm -fr dist/ build/
poetry build

twine check dist/*.tar.gz || exit 1
