#!/bin/sh

kega_libdir="/usr/lib/kega-fusion"
kega_sharedir="/usr/share/kega-fusion"
kega_localdir="$HOME/.Kega Fusion"

# create local plugins directory if not present
mkdir -p "$kega_localdir/Plugins"

# create links for every included plugin
if [ $(ls -1A $kega_libdir/plugins | wc -l) -gt 0 ]; then
  for i in $kega_libdir/plugins/*; do
    if [ ! -e "$kega_localdir/Plugins/$(basename "$i")" ]; then
      ln -sf "$i" "$kega_localdir/Plugins/"
    fi
  done
fi

# copy configuration file if not present
if ! [ -f "$kega_localdir/Fusion.ini" ]; then
  cp $kega_sharedir/Fusion.ini "$kega_localdir"
fi

# here we go!
$kega_libdir/Fusion "$@"
