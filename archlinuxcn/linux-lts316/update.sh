#!/bin/bash

set -eu

cd "$(dirname "$0")"

VERSION="$(curl -sSf https://www.kernel.org/releases.json | jq -r '.releases[].version' | grep '^3\.16\.')"
HASH="$(curl -sSf https://www.kernel.org/pub/linux/kernel/v3.x/sha256sums.asc | grep "patch-${VERSION}.xz" | cut -d' ' -f1)"

sed -i "s/pkgver=.*/pkgver=${VERSION}/" PKGBUILD
sed -i "s/.* # patch$/            '$HASH' # patch/" PKGBUILD
mksrcinfo
