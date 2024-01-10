#!/bin/bash

patches=(
    0001-adjust-buffer-format-order.patch
    0001-enable-linux-unstable-deb-target.patch
    0001-ozone-wayland-implement-text_input_manager-fixes.patch
    0001-ozone-wayland-implement-text_input_manager_v3.patch
    0001-vaapi-flag-ozone-wayland.patch
)

mkdir tmp
mv "${patches[@]}" tmp

rm ./*.patch
git clone https://gitlab.archlinux.org/archlinux/packaging/packages/chromium
mv chromium/*.patch .
nvim -d PKGBUILD chromium/PKGBUILD
makepkg --printsrcinfo > .SRCINFO
rm -rf chromium

mv tmp/* .
rmdir tmp
