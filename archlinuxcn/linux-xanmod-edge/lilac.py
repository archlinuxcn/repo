#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build('linux-xanmod-edge', maintainers=['figue'])

    # pkgrel is set to ${xanmod}
    for line in edit_file('PKGBUILD'):
        if line.startswith('pkgrel='):
            line = "pkgrel=1"
        print(line)
