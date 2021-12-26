#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers="atriix")

    for line in edit_file('PKGBUILD'):
        line = line.strip()
        if line.startswith('depends='):
            print('makedepends=(\'python-setuptools\')')
            line = line.replace(')', ' python-cffi)') # fix missing dependency
        print(line)
