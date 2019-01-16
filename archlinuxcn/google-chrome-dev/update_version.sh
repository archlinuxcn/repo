#!/bin/bash
set -euxo pipefail

# Get channel
CHANNEL=$(awk -F '=' '/^_channel/{ print $2 }' PKGBUILD)
PKG="google-chrome-${CHANNEL}"

# Get latest version
VER=$(curl -sL "https://dl.google.com/linux/chrome/rpm/stable/x86_64/repodata/other.xml.gz" | gzip -df |
	tr ' ' '\n' | grep -e name= -e ver= | cut -d '"' -f2 | sed 'N;s/\n/ /' |
	grep "${PKG}" | cut -d ' ' -f 2)

# Insert latest version into PKGBUILD and update hashes
sed -i \
	-e "s/^pkgver=.*/pkgver=${VER}/" \
	-e 's/pkgrel=.*/pkgrel=1/' \
	PKGBUILD
updpkgsums

# Check whether this changed anything
if (git diff --exit-code PKGBUILD); then
	echo "Package ${PKG} has most recent version ${VER}"
	exit 0
fi

# Update .SRCINFO
makepkg --printsrcinfo >.SRCINFO

# Commit changes
git add PKGBUILD .SRCINFO
git commit -m "${PKG} v${VER}"
