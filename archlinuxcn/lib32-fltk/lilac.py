#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build()
    add_depends(['lib32-libpng', 'libfontconfig.so'])
    add_provides(['libfltk.so', 'libfltk_forms.so', 'libfltk_gl.so', 'libfltk_images.so'])

def post_build():
    aur_post_build()
