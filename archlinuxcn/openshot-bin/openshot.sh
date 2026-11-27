#!/bin/bash
set -o pipefail
_APPDIR="/usr/lib/@appname@"
_RUNNAME="${_APPDIR}/@runname@"
export PATH="${_APPDIR}${PATH:+:$PATH}"
export LD_LIBRARY_PATH="${_APPDIR}:${_APPDIR}/lib${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
export QT_PLUGIN_PATH="${_APPDIR}/plugins${QT_PLUGIN_PATH:+:$QT_PLUGIN_PATH}"
export QML_IMPORT_PATH="${_APPDIR}/qml${QML_IMPORT_PATH:+:$QML_IMPORT_PATH}}"
export QML2_IMPORT_PATH="${_APPDIR}/qml${QML2_IMPORT_PATH:+:$QML2_IMPORT_PATH}}"
export QT_QPA_PLATFORMTHEME="gtk2"
cd "${_APPDIR}" || { echo "Failed to change directory to ${_APPDIR}"; exit 1; }
LD_PRELOAD=/usr/lib/libmpg123.so.0 exec "${_RUNNAME}" "$@" || exit $?