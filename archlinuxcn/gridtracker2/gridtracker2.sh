#!/bin/sh -eu

export NODE_ENV=production
exec /usr/bin/electron /usr/share/gridtracker2/resources/app.asar "$@"
