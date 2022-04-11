#!/bin/bash

export ELECTRON_IS_DEV=0
cd /usr/lib/joplin-desktop || exit 1
exec electron@electronversion@ /usr/lib/joplin-desktop/app.asar "$@"
