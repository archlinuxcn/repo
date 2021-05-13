#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers='rodrigo21')
    add_provides(['libmpeg2.so', 'libmpeg2convert.so'])

def post_build():
    aur_post_build()
