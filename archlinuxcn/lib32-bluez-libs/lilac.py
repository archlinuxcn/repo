#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers='WoefulDerelict')
    for line in edit_file('PKGBUILD'):
        print(line)
        if line.startswith('package_lib32-bluez-libs()'):
            print('  provides=("libbluetooth.so")')

def post_build():
    check_library_provides()
    aur_post_build()
