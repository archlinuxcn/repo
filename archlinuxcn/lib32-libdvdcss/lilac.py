#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers='GordonGR')
    add_provides(['libdvdcss.so'])

def post_build():
    check_library_provides()
    aur_post_build()
