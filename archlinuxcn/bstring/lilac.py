#!/usr/bin/env python3
from lilaclib import *

def pre_build():
    aur_pre_build('bstring', maintainers=['denn'])
    for line in edit_file('PKGBUILD'):
        if 'makedepends=' in line:
            line = "makedepends=('meson')"

        print(line)
