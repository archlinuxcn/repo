#!/bin/sh
export VCPKG_ROOT=/opt/vcpkg
export VCPKG_DOWNLOADS=/var/cache/vcpkg

$VCPKG_ROOT/vcpkg "$@"
