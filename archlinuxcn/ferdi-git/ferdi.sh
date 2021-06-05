#!/bin/sh

export NODE_ENV=production
exec electron '/usr/lib/ferdi/app.asar' "$@"
