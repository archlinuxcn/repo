#!/bin/bash

if [[ "$#" == '1' && "${1:0:1}" != '-' ]]; then
    exec /opt/gitkraken/gitkraken -p "$1"
else
    exec /opt/gitkraken/gitkraken "$@"
fi
