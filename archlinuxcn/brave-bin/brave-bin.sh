#!/usr/bin/env bash
XDG_CONFIG_HOME="${XDG_CONFIG_HOME:-$HOME/.config}"

# Allow users to override command-line options
USER_FLAGS_FILE="$XDG_CONFIG_HOME/brave-flags.conf"
if [[ -f $USER_FLAGS_FILE ]]; then
   USER_FLAGS="$(cat $USER_FLAGS_FILE | sed 's/#.*//')"
fi

if [[ -f /proc/sys/kernel/unprivileged_userns_clone && $(< /proc/sys/kernel/unprivileged_userns_clone) == 0 ]]; then
    >&2 echo "User namespaces are detected as disabled on your system, Brave will run with the sandbox disabled"
    SANDBOX_FLAG="--no-sandbox"
fi

exec /usr/lib/brave-bin/brave "$@" $SANDBOX_FLAG $USER_FLAGS
