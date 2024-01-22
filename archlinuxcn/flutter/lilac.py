#!/usr/bin/python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['frealgagu','WithTheBraid','PolarianDev'])

    for line in edit_file('PKGBUILD'):
        if line.startswith('license='):
            line = "license=('BSD-3-Clause')"
        print(line)
