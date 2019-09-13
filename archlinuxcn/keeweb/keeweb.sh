#!/usr/bin/sh

exec electron /usr/lib/keeweb/app.asar --disable-updater "$@"
