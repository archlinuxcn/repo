#!/bin/bash

mkdir tmp
mv ozone-add-va-api-support-to-wayland.patch remove-main-main10-profile-limit.patch skia-gamma.patch vaapi-add-av1-support.patch tmp

rm *.patch
git clone https://gitlab.archlinux.org/archlinux/packaging/packages/chromium
mv chromium/*.patch .
nvim -d PKGBUILD chromium/PKGBUILD
makepkg --printsrcinfo > .SRCINFO
rm -rf chromium

mv tmp/* .
rmdir tmp
