#!/usr/bin/python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['That1Calculator'])

    for line in edit_file('PKGBUILD'):
        print (line.replace('livglvnd', 'libglvnd'))
