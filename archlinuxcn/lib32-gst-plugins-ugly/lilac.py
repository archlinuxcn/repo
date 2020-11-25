#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build()
    add_depends(['liba52.so', 'libcdio.so', 'libdvdread.so', 'libglib-2.0.so', 'libgmodule-2.0.so', 'libgobject-2.0.so', 'libmpeg2.so', 'libopencore-amrnb.so', 'libopencore-amrwb.so', 'libsidplay.so', 'libx264.so'])

def post_build():
    aur_post_build()
