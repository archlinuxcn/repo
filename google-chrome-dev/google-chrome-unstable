#!/bin/bash

# Allow users to override command-line options
if [[ -f ~/.config/chrome-dev-flags.conf ]]; then
   CHROME_USER_FLAGS="$(cat ~/.config/chrome-dev-flags.conf)"
fi

# Launch
exec /opt/google/chrome-unstable/google-chrome-unstable $CHROME_USER_FLAGS "$@"