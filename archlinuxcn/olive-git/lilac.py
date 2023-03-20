#!/usr/bin/python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['tecnotercio'])

    for line in edit_file('PKGBUILD'):
        print (line.replace('opentimelineio0.14', 'opentimelineio-git'))
