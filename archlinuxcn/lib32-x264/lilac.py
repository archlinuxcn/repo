#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers='oxalin')
    add_depends(['liblsmash.so'])
    for line in edit_file('PKGBUILD'):
        print(line.replace('x264=', 'x264>='))

def post_build():
    check_library_provides()
    aur_post_build()
