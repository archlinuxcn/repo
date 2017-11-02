#!/bin/bash
set -e

pkgver=$(bash ./check_ver.sh)
sed "s/^pkgver=.*/pkgver=$pkgver/" -i PKGBUILD
updpkgsums
