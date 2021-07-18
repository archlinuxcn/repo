#!/bin/bash

mkdir tmp
mv wayland-egl.patch tmp

rm *.patch
git clone https://github.com/archlinux/svntogit-packages.git --branch packages/chromium --single-branch chr
mv chr/trunk/*.patch .
rm -rf chr

mv tmp/* .
rmdir tmp
