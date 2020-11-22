#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build()
    for line in edit_file('PKGBUILD'):
        print(line)
        if line.startswith('package_lib32-bluez-libs()'):
            print('  provides=("libbluetooth.so")')

def post_build():
    aur_post_build()
