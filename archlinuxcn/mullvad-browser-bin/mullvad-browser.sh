#!/bin/sh

XDG_CONFIG_HOME="${XDG_CONFIG_HOME:-$HOME/.config}"

# Allow users to override command-line options
USER_FLAGS_FILE="$XDG_CONFIG_HOME/mullvad-browser-flags.conf"

if [ -f "$USER_FLAGS_FILE" ]; then
  USER_FLAGS="$(sed 's/#.*//' "$USER_FLAGS_FILE" | tr '\n' ' ')"
fi

# Do not (try to) connect to the session manager
unset SESSION_MANAGER

# Set up custom bundled fonts. See fonts-conf(5).
export FONTCONFIG_PATH="/opt/mullvad-browser/fontconfig"
export FONTCONFIG_FILE="fonts.conf"

# tor-browser-build#41017: Nvidia drivers create a shader cache by default in
# $HOME/.cache/nvidia. We we can easily disable it.
export __GL_SHADER_DISK_CACHE=0

exec /opt/mullvad-browser/mullvadbrowser "$@" $USER_FLAGS
