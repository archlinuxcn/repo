#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers='rodrigo21')
    add_provides(['libmms.so'])

def post_build():
    check_library_provides()
    aur_post_build()
