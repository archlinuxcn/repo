#!/bin/bash

if (( $# != 1 )); then
    echo "Usage: $0 VERSION"
    echo "Update pkgver to VERSION and then build and commit."
    echo "You just need to test the package, review the commit and push."
    exit 1
fi

VERSION=$1

set -x

sed -i "s/^pkgver=.*\$/pkgver=${VERSION}/" PKGBUILD
updpkgsums
makepkg --printsrcinfo > .SRCINFO
git add .
git commit -m "Upgrade to v${VERSION}"
makepkg
sudo pacman -U nvm-${VERSION}-1-any.pkg.tar.xz

set +x

echo "Now smoke test the package, review the commit, and push"
