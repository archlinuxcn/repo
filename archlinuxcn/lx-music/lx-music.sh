#!/bin/sh
XDG_CONFIG_HOME=${XDG_CONFIG_HOME:-~/.config}

# Allow users to override command-line options
if [[ -f $XDG_CONFIG_HOME/lx-music-flags.conf ]]; then
   LX_USER_FLAGS="$(sed 's/#.*//' $XDG_CONFIG_HOME/lx-music-flags.conf | tr '\n' ' ')"
fi

# DO NOT change __ELECTRON__, it's updated by PKGBUILD
exec __ELECTRON__ /usr/lib/lx-music/ "$@" $LX_USER_FLAGS
