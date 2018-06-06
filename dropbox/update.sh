#!/bin/bash
set -e

pkgver=$(python ./check_ver.py)
sed "s/^pkgver=.*/pkgver=$pkgver/;s/^pkgrel=.*/pkgrel=1/" -i PKGBUILD
updpkgsums
