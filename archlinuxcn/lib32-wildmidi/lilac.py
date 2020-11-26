#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build()
    add_depends(['libasound.so'])
    add_provides(['libWildMidi.so'])
    for line in edit_file('PKGBUILD'):
        stripped_line = line.strip()
        if stripped_line != 'mv lib lib32':
            print(line)
        if stripped_line.startswith('cmake '):
            print('        -DLIB_SUFFIX=32 \\')

def post_build():
    aur_post_build()
