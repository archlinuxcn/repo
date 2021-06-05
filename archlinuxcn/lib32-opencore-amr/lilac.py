#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers='morguldir')
    add_depends(['lib32-glibc'])
    add_provides(['libopencore-amrnb.so', 'libopencore-amrwb.so'])

def post_build():
    check_library_provides()
    aur_post_build()
