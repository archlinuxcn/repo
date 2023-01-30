#!/usr/bin/env fish

set -l package_version $argv[1]

sed -E "s/pkgver=.*\$/pkgver=$package_version/g" -i PKGBUILD
updpkgsums
makepkg --printsrcinfo > .SRCINFO
makepkg
