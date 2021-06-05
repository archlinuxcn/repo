#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers='llde')
    add_provides(['liblavfile-${pkgver%.*}.so', 'liblavjpeg-${pkgver%.*}.so', 'liblavplay-${pkgver%.*}.so', 'libmjpegutils-${pkgver%.*}.so', 'libmpeg2encpp-${pkgver%.*}.so', 'libmplex2-${pkgver%.*}.so'])

def post_build():
    check_library_provides()
    aur_post_build()
