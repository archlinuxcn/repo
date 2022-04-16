#!/usr/bin/env sh
set -eu

pkgname=powder-toy
data_home="${XDG_DATA_HOME:-${HOME}/.local/share}/${pkgname}"

mkdir -p "${data_home}"
cd "${data_home}"
exec "/usr/lib/${pkgname}/${pkgname}" "$@"
