#!/bin/bash
if [[ $EUID -ne 0 ]] || [[ $ELECTRON_RUN_AS_NODE ]]; then
    exec electron19 /usr/lib/balena-etcher "$@"
else
    exec electron19 --no-sandbox /usr/lib/balena-etcher "$@"
fi
