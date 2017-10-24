#!/bin/bash

PACKAGE_NAME="ieaseMusic"
EW_DIR="/opt/$PACKAGE_NAME"

cd "$EW_DIR" || exit 1
exec electron . "$@"
