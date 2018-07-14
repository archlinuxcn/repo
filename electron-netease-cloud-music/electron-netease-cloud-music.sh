#!/bin/bash

PACKAGE_NAME="electron-netease-cloud-music"
EW_DIR="/usr/lib/$PACKAGE_NAME/electron-netease-cloud-music.asar"

exec electron $EW_DIR

#cd "$EW_DIR" || exit 1
#exec electron . "$@"
