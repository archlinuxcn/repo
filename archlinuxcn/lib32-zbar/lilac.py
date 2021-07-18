#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers='llde')
    add_depends(['libdbus-1.so', 'libjpeg.so'])
    add_provides(['libzbar.so'])


def post_build():
    check_library_provides()
    aur_post_build()
