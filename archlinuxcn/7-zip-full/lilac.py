#!/usr/bin/python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['Hanabishi'])
    for line in edit_file('PKGBUILD'):
        if line.startswith('license='):
            line = "license=('LGPL-2.1-or-later AND BSD-3-Clause AND LicenseRef-unRAR')"
        print(line)
