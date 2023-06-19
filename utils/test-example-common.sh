#!/bin/sh

EXAMPLE_DIR="${1:?missing example directory}"

set -xe

cd "$EXAMPLE_DIR"
NO_DOWNLOAD=1 ./update-schema.sh
./update-operations.sh
