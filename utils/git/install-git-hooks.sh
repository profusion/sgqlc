#!/bin/sh

SELF=`basename $0`
HOOKS_DIR=`dirname $PWD/$0`

for F in $HOOKS_DIR/*; do
    HOOK_NAME=`basename $F`
    if [ $SELF != $HOOK_NAME ] && [ -x $F ]; then
        echo "installing $F as .git/hooks/$HOOK_NAME"
        ln -sf $F .git/hooks/$HOOK_NAME
    fi
done
