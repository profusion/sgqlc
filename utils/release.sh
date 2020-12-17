#!/bin/bash

if [ "$PIPENV_ACTIVE" = "1" ]; then
  # bin/* scripts shebang is being replaced with current venv
  echo "exit pipenv before generating the package" >&2
  exit 1
fi

SETUP_VERSION=`./setup.py --version`
MOD_VERSION=`PYTHONPATH='.' python3 -c 'import sgqlc; print(sgqlc.__version__)'`
if [ $SETUP_VERSION != $MOD_VERSION ]; then
  echo "update both setup.py and sgqlc/__init__.py so versions match" >&2
  exit 1
fi

rm -fr dist/ build
./setup.py egg_info -Db '' sdist bdist_wheel bdist_egg

twine check dist/*.tar.gz || exit 1
