#!/usr/bin/env bash

#
# This script is used to semi-automatically run a build and update the PKGBUILD file locally.
# It is not used in the AUR builds in any way, and is only for manual releasing purposes.
#

set -e

rm -rf ferdium-*.pkg.tar.zst
makepkg
makepkg --printsrcinfo > .SRCINFO
newversion=$(grep pkgver .SRCINFO | awk -F= '{print $2}' | sed -e 's/ //g')
git commit -am "Updated to ${newversion}."
