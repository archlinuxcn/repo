#!/bin/bash

# Substitute XDG_CONFIG_HOME by ~/.config if the env var is unset or empty
XDG_CONFIG_HOME=${XDG_CONFIG_HOME:-~/.config}

# Allow users to override command-line options
if [[ -f "${XDG_CONFIG_HOME}/spotify-flags.conf" ]]; then
    mapfile -t SPOTIFY_USER_FLAGS <<< "$(grep -v '^#' "${XDG_CONFIG_HOME}/spotify-flags.conf")"
    echo "User flags:" "${SPOTIFY_USER_FLAGS[@]}"
fi

# Launch Spotify with the given flags
exec /opt/spotify/spotify "${SPOTIFY_USER_FLAGS[@]}" "$@"
