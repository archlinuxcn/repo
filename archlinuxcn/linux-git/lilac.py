#!/usr/bin/python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['osimarr'])
    add_makedepends(['python'])

    for line in edit_file('PKGBUILD'):
        if line.strip().startswith('printf'):
            print(line.replace("sed \'s/\\([^-]*-\\)g/r\\1/;s/-/./g\'", "sed \'s/\\([^-]*-\\)g/r\\1/;s/-/./g;s/v//\'"))
        else:
            print(line)
