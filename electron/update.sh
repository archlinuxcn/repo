#!/usr/bin/env bash
# PKGBUILD update script for https://aur.archlinux.org/packages/electron/
# Maintainer: /dev/rs0 <rs0@secretco.de.com>

URL="https://github.com/electron/electron/releases"
VERSION="$(curl -s ${URL}/latest | sed -e 's/.*\/tag\/v//' | cut -d\" -f1)"
FILE_URL="${URL}/download/v${VERSION}"
FILE_arm="electron-v${VERSION}-linux-arm.zip"
FILE_i686="electron-v${VERSION}-linux-ia32.zip"
FILE_x86_64="electron-v${VERSION}-linux-x64.zip"

echo "Found version ${VERSION}."
sed -i -e 's/pkgver=.*/pkgver='${VERSION}'/' PKGBUILD
sed -i -e 's/pkgrel=.*/pkgrel=1/' PKGBUILD
echo "Downloading ${FILE_arm}..."
sed -i -e "s/_arch='arm' ; sha256sums=('.*/_arch='arm' ; sha256sums=('`curl -L ${FILE_URL}/${FILE_arm} | sha256sum | cut -d' ' -f1`');;/" PKGBUILD
echo "Downloading ${FILE_i686}..."
sed -i -e "s/_arch='ia32'; sha256sums=('.*/_arch='ia32'; sha256sums=('`curl -L ${FILE_URL}/${FILE_i686} | sha256sum | cut -d' ' -f1`');;/" PKGBUILD
echo "Downloading ${FILE_x86_64}..."
sed -i -e "s/_arch='x64' ; sha256sums=('.*/_arch='x64' ; sha256sums=('`curl -L ${FILE_URL}/${FILE_x86_64} | sha256sum | cut -d' ' -f1`');;/" PKGBUILD
mksrcinfo
echo "PKGBUILD updated!"
