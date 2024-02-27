#!/usr/bin/python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['encounter','class101','nullableVoidPtr'])

    for line in edit_file('PKGBUILD'):
        if line.startswith('license='):
            line = "license=('Apache-2.0')"
        print (line.replace('java-environment>=17','java-environment=17'))
