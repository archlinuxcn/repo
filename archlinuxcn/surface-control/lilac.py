#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build()
    for line in edit_file('PKGBUILD'):
        if line.startswith('makedepends='):
            line = '#' + line + '\n' + "makedepends=('cargo' 'git' 'rust' 'systemd')"
        print(line)
