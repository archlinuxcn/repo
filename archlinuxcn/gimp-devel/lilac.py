#!/usr/bin/python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['twa022'])

    for line in edit_file('PKGBUILD'):
        if line.startswith('license='):
            line = "license=('GPL-3.0-or-later')"
        print(line)
