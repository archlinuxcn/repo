#!/bin/sh
export VCPKG_ROOT=/usr/share/vcpkg
export VCPKG_DOWNLOADS=/var/cache/vcpkg

$VCPKG_ROOT/vcpkg "$@"
