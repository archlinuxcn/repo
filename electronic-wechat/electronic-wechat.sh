#!/bin/bash

PACKAGE_NAME="electronic-wechat"
EW_DIR="/usr/lib/$PACKAGE_NAME"

cd "$EW_DIR" || exit 1
exec electron . "$@"
