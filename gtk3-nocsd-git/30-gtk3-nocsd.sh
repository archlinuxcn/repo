#!/bin/bash

if [ -n "${GNOME_DESKTOP_SESSION_ID-}" ]; then
    # just in case DESKTOP_SESSION wasn't properly set
    _check=gnome
else
    _check="${DESKTOP_SESSION-}"
fi

case "${_check}" in

    gnome|gnome-*|*/gnome|*/gnome-*)
        unset GTK_CSD
    ;;

    *)
        export GTK_CSD=0
        export LD_PRELOAD="/usr/\${LIB}/libgtk3-nocsd.so.0${LD_PRELOAD:+:$LD_PRELOAD}"
    ;;
esac

unset _check
