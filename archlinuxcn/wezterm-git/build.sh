#!/bin/bash
set -e
set -x
makepkg --force --syncdeps --noconfirm
makepkg --printsrcinfo > .SRCINFO
namcap PKGBUILD
namcap wezterm*.pkg.tar.xz
