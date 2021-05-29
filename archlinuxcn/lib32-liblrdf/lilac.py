#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers='rodrigo21')
    add_depends(['libraptor2.so'])
    add_provides(['liblrdf.so'])

def post_build():
    check_library_provides()
    aur_post_build()
