#!/bin/sh
if [ "$1" = "" -o ! -e "$1" ]; then
    echo "no package supplied" 1>&2
   exit 1
fi
bsdtar xf $1
