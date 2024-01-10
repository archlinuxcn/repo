#!/bin/bash

XDG_CONFIG_HOME=${XDG_CONFIG_HOME:-~/.config}

# Allow users to override command-line options
if [[ -f $XDG_CONFIG_HOME/codium-flags.conf ]]; then
    readarray lines <"$XDG_CONFIG_HOME/codium-flags.conf"
    for line in "${lines[@]}"; do
        if ! [[ "$line" =~ ^[[:space:]]*# ]]; then
           CODE_USER_FLAGS+=($line)
        fi
    done
fi

# Launch
exec /opt/vscodium-bin/bin/codium "$@" "${CODE_USER_FLAGS[@]}"
