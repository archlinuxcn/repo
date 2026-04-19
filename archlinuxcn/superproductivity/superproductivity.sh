#!/bin/bash
set -o pipefail
_APPDIR="/usr/lib/@appname@"
_RUNNAME="${_APPDIR}/@runname@"
_CFGDIR="@cfgdirname@/"
_OPTIONS="@options@"
export PATH="${_APPDIR}:${PATH}"
export LD_LIBRARY_PATH="${_APPDIR}/swiftshader:${_APPDIR}/lib:${LD_LIBRARY_PATH}"
export ELECTRON_IS_DEV=0
export ELECTRON_FORCE_IS_PACKAGED=true
export ELECTRON_DISABLE_SECURITY_WARNINGS=true
export ELECTRON_OVERRIDE_DIST_PATH="/usr/bin/electron@electronversion@"
export NODE_ENV=production
export XDG_CONFIG_HOME="${XDG_CONFIG_HOME:-$HOME/.config}"
export _FLAGS_FILE="${XDG_CONFIG_HOME}/${_CFGDIR}@appname@-flags.conf"
declare -a _USER_FLAGS
if [[ -f "${_FLAGS_FILE}" ]]; then
    while read -r line; do
        if [[ ! "${line}" =~ ^[[:space:]]*#.* ]]; then
            _USER_FLAGS+=("${line}")
        fi
    done < "${_FLAGS_FILE}"
fi
cd "${_APPDIR}" || { echo "Failed to change directory to ${_APPDIR}"; exit 1; }
if [[ "${EUID}" -ne 0 ]] || [[ "${ELECTRON_RUN_AS_NODE}" ]]; then
    exec electron@electronversion@ "${_RUNNAME}" ${_OPTIONS} "${_USER_FLAGS[@]}" "$@"
else
    exec electron@electronversion@ "${_RUNNAME}" ${_OPTIONS} --no-sandbox "${_USER_FLAGS[@]}" "$@"
fi