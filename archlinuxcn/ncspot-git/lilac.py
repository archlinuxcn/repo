#!/usr/bin/env python3
from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['gugylucky'])
    add_makedepends(['git'])

    for line in edit_file('PKGBUILD'):
        if "pkgname=" in line:
            # upstream added, dont need lto anymore
            #print("options=(!lto)")
            # version number somehow become .1.1.0-1,
            # add epoch to force pacman update
            print("epoch=1")
        print(line)
