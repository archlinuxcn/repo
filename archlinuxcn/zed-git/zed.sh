#!/usr/bin/env bash

if [[ $1 == http://* ]] || [[ $1 == https://* ]]; then
    PROJECT=$1
elif [ "" != "$1" ]; then
   PROJECT=$(readlink -f $1)
fi

nw /usr/share/zed-git/app.nw/ $PROJECT 2> /dev/null
