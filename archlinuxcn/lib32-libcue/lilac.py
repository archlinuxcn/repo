#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers='GordonGR')
    add_provides(['libcue.so'])

def post_build():
    aur_post_build()
