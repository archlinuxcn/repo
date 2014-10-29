#!/bin/sh
CC=${CC:-gcc}
[[ $CC =~ clang ]] && set -- "${@//-fvar-tracking-assignments/-g}"
$CC "${@}" -I"${__PYZMQ_PKGDIR}/site-packages/zmq/utils" \
    -I"${__PYZMQ_PKGDIR}/site-packages/zmq/backend/cython" \
    -I"${__PYZMQ_PKGDIR}/site-packages/zmq/devices"
