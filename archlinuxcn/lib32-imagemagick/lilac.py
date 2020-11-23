#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build()
    add_depends(['libIlmImf-2_5.so', 'libfontconfig.so', 'libfreetype.so', 'libglib-2.0.so', 'libgobject-2.0.so', 'libheif.so', 'libjpeg.so', 'liblqr-1.so', 'libopenjp2.so', 'libpango-1.0.so', 'libpangocairo-1.0.so', 'libraqm.so', 'libraw_r.so', 'librsvg-2.so', 'libwmflite-0.2.so'])
    add_provides(['libMagick++-${pkgver%%.*}.Q16HDRI.so', 'libMagickCore-${pkgver%%.*}.Q16HDRI.so', 'libMagickWand-${pkgver%%.*}.Q16HDRI.so'])

def post_build():
    aur_post_build()
