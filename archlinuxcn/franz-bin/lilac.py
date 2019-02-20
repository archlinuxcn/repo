#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build()

    for line in edit_file('PKGBUILD'):
        line = line.strip()
        if line.startswith('pkgver=') and "_" not in line:
            print("_" + line + "_release")
        else if line.startswith('package()'):
            print("pkgver=$_pkgver")
        print(line)
