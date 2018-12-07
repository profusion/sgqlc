#!/bin/bash

if [ "$PIPENV_ACTIVE" = "1" ]; then
  # bin/* scripts shebang is being replaced with current venv
  echo "exit pipenv before generating the package" >&2
  exit 1
fi

rm -fr dist/ build
./setup.py egg_info -Db '' sdist bdist_wheel
