#!/bin/bash

set -eu

cd "$(dirname "$0")"

RELEASES_URL="https://www.kernel.org/releases.json"
SHA256SUMS_URL="https://www.kernel.org/pub/linux/kernel/v4.x/sha256sums.asc"

VERSION="$(curl -sSLf "$RELEASES_URL" |
    jq -r '[.releases[].version] | map(select(startswith("4.4.")))[]')"

HASH="$(curl -sSLf "$SHA256SUMS_URL" |
    awk "\$2 == \"patch-$VERSION.xz\" {print \$1}")"

sed -i \
    -e "s/pkgver=.*/pkgver=${VERSION}/" \
    -e "s/.* # patch$/            '$HASH' # patch/" \
    PKGBUILD

makepkg --printsrcinfo > .SRCINFO

git add -u
if ! git diff-index --quiet HEAD; then
    git commit -m "Updated to $VERSION"
fi
