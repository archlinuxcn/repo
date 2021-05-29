#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers='quartic')
    add_depends(['libgif.so', 'libjpeg.so'])
    add_provides(['libjbig2enc.so'])

def post_build():
    check_library_provides()
    aur_post_build()
