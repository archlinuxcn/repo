#!/bin/sh

XDG_CONFIG_HOME=${XDG_CONFIG_HOME:-~/.config}

# Allow users to override command-line options
if [[ -f $XDG_CONFIG_HOME/vesktop-flags.conf ]]; then
    VESKTOP_USER_FLAGS="$(grep -v '^#' $XDG_CONFIG_HOME/vesktop-flags.conf)"
fi

# Launch
exec /usr/lib/vesktop/vesktop $VESKTOP_USER_FLAGS "$@"
