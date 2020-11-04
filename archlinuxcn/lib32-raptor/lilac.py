#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build()
    add_depends(['libicudata.so', 'libicui18n.so', 'libicuuc.so'])
    add_provides(['libraptor2.so'])

def post_build():
    aur_post_build()
