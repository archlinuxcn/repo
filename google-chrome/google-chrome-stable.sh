#!/bin/bash

# Allow users to override command-line options
if [[ -f ~/.config/chrome-flags.conf ]]; then
   CHROME_USER_FLAGS="$(cat ~/.config/chrome-flags.conf)"
fi

# Launch
exec /opt/google/chrome/google-chrome $CHROME_USER_FLAGS "$@"