#!/bin/sh

XMIND_USER_FLAGS_FILE="${XDG_CONFIG_HOME:-$HOME/.config}/Xmind/user-flags.conf"

# Allow users to override command-line options
if [[ -f "${XMIND_USER_FLAGS_FILE}" ]]; then
   XMIND_USER_FLAGS=$(grep -v '^#' "$XMIND_USER_FLAGS_FILE")
fi

# Launch
exec /opt/Xmind/xmind $XMIND_USER_FLAGS "$@"
