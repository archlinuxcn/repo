#!/bin/bash

XFT_SETTINGS="
Xft.antialias:  1
Xft.autohint:   0
Xft.dpi:        96
Xft.hinting:    1
Xft.hintstyle:  hintslight
Xft.lcdfilter:  lcddefault
Xft.rgba:       rgb
"

echo "$XFT_SETTINGS" | xrdb -merge > /dev/null 2>&1

# vim:ft=sh:
