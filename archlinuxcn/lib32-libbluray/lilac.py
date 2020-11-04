#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build()
    add_depends(['libfontconfig.so', 'libfreetype.so'])
    add_provides(['libbluray.so'])

def post_build():
    aur_post_build()
