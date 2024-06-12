#!/usr/bin/env bash

makepkg -ofC

readonly SDK_VERSION="$(cat src/dart/dart-sdk/version)"

sed -i 's/_dartver=.*/_dartver="'"${SDK_VERSION}"'"/g' PKGBUILD

