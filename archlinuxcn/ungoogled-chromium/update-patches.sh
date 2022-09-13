#!/bin/bash

mkdir tmp
mv ozone-add-va-api-support-to-wayland.patch remove-main-main10-profile-limit.patch tmp

rm *.patch
git clone https://github.com/archlinux/svntogit-packages.git --branch packages/chromium --single-branch chr
mv chr/trunk/*.patch .
nvim -d PKGBUILD chr/trunk/PKGBUILD
makepkg --printsrcinfo > .SRCINFO
rm -rf chr

mv tmp/* .
rmdir tmp
