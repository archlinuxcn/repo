#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers='rodrigo21')
    add_depends(['libavcodec.so', 'libavutil.so'])
    add_provides(['libchromaprint.so'])

def post_build():
    check_library_provides()
    aur_post_build()
