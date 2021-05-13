#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers='adam900710')
    add_depends(['libfontconfig.so', 'libfreetype.so', 'libfribidi.so', 'libharfbuzz.so'])

def post_build():
    aur_post_build()
