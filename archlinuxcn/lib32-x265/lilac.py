#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers='llde')
    add_depends(['libnuma.so'])
    add_makedepends(['git'])

def post_build():
    check_library_provides()
    aur_post_build()
