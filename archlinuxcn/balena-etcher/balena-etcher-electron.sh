#!/bin/bash
if [[ $EUID -ne 0 ]] || [[ $ELECTRON_RUN_AS_NODE ]]; then
    exec _ELECTRON_ /usr/lib/balena-etcher "$@"
else
    exec _ELECTRON_ --no-sandbox /usr/lib/balena-etcher "$@"
fi
