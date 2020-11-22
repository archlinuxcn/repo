#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build()
    add_depends(['lib32-aom', 'libaom.so', 'libde265.so', 'libgdk_pixbuf-2.0.so', 'libglib-2.0.so', 'libgobject-2.0.so', 'libx265.so'])
    add_provides(['libheif.so'])

def post_build():
    aur_post_build()
