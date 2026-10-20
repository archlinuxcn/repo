#!/bin/sh
exec env -u ELECTRON_FORCE_IS_PACKAGED /usr/lib/electron44/electron /usr/lib/lceda-pro/resources/app/ "$@"
