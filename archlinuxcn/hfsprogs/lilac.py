#!/usr/bin/python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['muflone'])
    for line in edit_file('PKGBUILD'):
        if line.startswith('license='):
            line = "license=('APSL-2.0')"
        print(line)
