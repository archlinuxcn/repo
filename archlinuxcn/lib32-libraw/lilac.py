#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build()
    add_depends(['libjasper.so', 'libjpeg.so'])
    add_provides(['libraw.so', 'libraw_r.so'])
    for line in edit_file('PKGBUILD'):
        if not line.startswith('makedepends='):
            print(line)

def post_build():
    aur_post_build()
