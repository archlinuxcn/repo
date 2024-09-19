#!/usr/bin/env python3

from lilaclib import aur_pre_build
from lilaclib import edit_file


def pre_build():
    aur_pre_build()
    with open('PKGBUILD', 'r') as f:
        if not any(line.startswith('provides=') for line in f):
            for line in edit_file("PKGBUILD"):
                if line.startswith('conflicts='):
                    line = "provides=('apparmor.d')\n" + line
                print(line)
