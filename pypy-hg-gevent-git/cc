#!/bin/sh
CC=${CC:-gcc}
[[ $CC =~ clang ]] && set -- "${@//-fvar-tracking-assignments/-g}"
$CC "${@}" -I"${__GEVENT_PKGDIR}/libev" \
    -I"${__GEVENT_PKGDIR}" -I"${__GEVENT_PKGDIR2}/libev" \
    -I"${__GEVENT_PKGDIR2}"
