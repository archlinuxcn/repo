#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers='rodrigo21')
    add_depends(['libfontconfig.so', 'libfreetype.so', 'libfribidi.so', 'libharfbuzz.so'])
    add_provides(['libass.so'])

def post_build():
    check_library_provides()
    aur_post_build()
