#!/usr/bin/env bash
#
# A helper script to allow the use of custom flags
#
# ------------------------------------------------------------------------------
# Usage
# ------------------------------------------------------------------------------
# Create a new file ~/.config/ticktick-flags.conf
# Add one flag per line into the file
# Comment lines will be ignored
# ------------------------------------------------------------------------------

# Substitute XDG_CONFIG_HOME by ~/.config if the env var is unset or empty
XDG_CONFIG_HOME=${XDG_CONFIG_HOME:-~/.config}

# Allow users to override command-line options
if [[ -f "${XDG_CONFIG_HOME}/ticktick-flags.conf" ]]; then
    mapfile -t TICKTICK_USER_FLAGS <<< "$(grep -v '^#' "${XDG_CONFIG_HOME}/ticktick-flags.conf")"
    echo "User flags:" "${TICKTICK_USER_FLAGS[@]}"
fi

# Launch TickTick
exec /opt/TickTick/ticktick "${TICKTICK_USER_FLAGS[@]}" "${@}"
