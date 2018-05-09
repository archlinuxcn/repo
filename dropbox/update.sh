#!/bin/bash
set -e

pkgver=$(python ./check_ver.py)
sed "s/^pkgver=.*/pkgver=$pkgver/" -i PKGBUILD
updpkgsums
