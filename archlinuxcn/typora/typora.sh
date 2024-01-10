#!/bin/bash

XDG_CONFIG_HOME=${XDG_CONFIG_HOME:-~/.config}

# Allow users to override command-line options
if [[ -f $XDG_CONFIG_HOME/typora-flags.conf ]]; then
	TYPORA_USER_FLAGS="$(sed 's/#.*//' $XDG_CONFIG_HOME/typora-flags.conf | tr '\n' ' ')"
fi

# Launch
exec /usr/share/typora/Typora "$@" $TYPORA_USER_FLAGS
