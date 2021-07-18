#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers='frealgagu')
    add_provides(['libcdio++.so', 'libcdio.so', 'libiso9660++.so', 'libiso9660.so', 'libudf.so'])

def post_build():
    check_library_provides()
    aur_post_build()
