#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build()
    add_depends(['libfreetype.so', 'libfribidi.so', 'libharfbuzz.so'])
    add_provides(['libraqm.so'])

def post_build():
    aur_post_build()
