#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers='rodrigo21')
    for line in edit_file('PKGBUILD'):
        if line.startswith('pkgver()'):
            print('_' + line)
        else:
            print(line)
    add_provides(['libsrtp2.so'])

def post_build():
    check_library_provides()
    aur_post_build()
