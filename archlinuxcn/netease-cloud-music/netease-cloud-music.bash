#!/bin/sh
HERE="$(dirname "$(readlink -f "${0}")")"
export LD_LIBRARY_PATH="${HERE}"/libs
export QT_PLUGIN_PATH="${HERE}"/plugins 
export QT_QPA_PLATFORM_PLUGIN_PATH="${HERE}"/plugins/platforms
export QT_QPA_PLATFORM=xcb
export LD_PRELOAD="${HERE}"/libnetease-patch.so

exec "${HERE}"/netease-cloud-music $@
