#!/bin/bash

XDG_CONFIG_HOME=${XDG_CONFIG_HOME:-~/.config}

# Allow users to override command-line options
if [[ -f $XDG_CONFIG_HOME/codium-flags.conf ]]; then
    IFS=' ' read -ra CODE_USER_FLAGS < "$XDG_CONFIG_HOME/codium-flags.conf"
fi

# Launch
exec /opt/vscodium-bin/bin/codium "$@" "${CODE_USER_FLAGS[@]}"
