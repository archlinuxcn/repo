#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers='dbermond')
    add_provides(['libmp3lame.so'])

def post_build():
    aur_post_build()
