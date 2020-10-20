#!/bin/bash
set -euxo pipefail

# Get channel
CHANNEL=$(awk -F '=' '/^_channel/{ print $2 }' PKGBUILD)
PKG="google-chrome-${CHANNEL}"

# Get latest version
VER=$(curl -sSf https://dl.google.com/linux/chrome/deb/dists/stable/main/binary-amd64/Packages |
	grep -A1 "Package: ${PKG}" |
	awk '/Version/{print $2}' |
	cut -d '-' -f1)

# Insert latest version into PKGBUILD and update hashes
sed -i \
	-e "s/^pkgver=.*/pkgver=${VER}/" \
	-e 's/pkgrel=.*/pkgrel=1/' \
	PKGBUILD

# Check whether this changed anything
if (git diff --exit-code PKGBUILD); then
	echo "Package ${PKG} has most recent version ${VER}"
	exit 0
fi

updpkgsums

# Update .SRCINFO
makepkg --printsrcinfo >.SRCINFO

# Commit changes
git add PKGBUILD .SRCINFO
git commit -m "${PKG} v${VER}"
