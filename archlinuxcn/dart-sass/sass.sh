#!/usr/bin/sh

INSTALL_NAME="sass"
DIR="/usr/lib/${INSTALL_NAME}"

cd "${DIR}" || exit 1
exec /usr/bin/dart ./app.snapshot "${@}"
