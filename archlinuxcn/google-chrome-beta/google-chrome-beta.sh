#!/bin/bash

XDG_CONFIG_HOME=${XDG_CONFIG_HOME:-~/.config}

# Allow users to override command-line options
if [[ -f $XDG_CONFIG_HOME/chrome-beta-flags.conf ]]; then
	CHROME_USER_FLAGS="$(cat $XDG_CONFIG_HOME/chrome-beta-flags.conf)"
fi

# Launch
exec /opt/google/chrome-beta/google-chrome-beta $CHROME_USER_FLAGS "$@"
