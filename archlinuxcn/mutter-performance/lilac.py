#!/usr/bin/python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['Terence','glorious-yellow'])
    for line in edit_file('PKGBUILD'):
        if line.startswith('pkgrel='):
            print("epoch=1")
        print(line.replace('groups=(gnome)', ''))
