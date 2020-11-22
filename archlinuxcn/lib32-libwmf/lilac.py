#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build()
    add_depends(['lib32-libx11', 'libfreetype.so', 'libglib-2.0.so', 'libgobject-2.0.so'])
    add_provides(['libwmf-${pkgver%.*}.so', 'libwmflite-${pkgver%.*}.so'])

def post_build():
    aur_post_build()
