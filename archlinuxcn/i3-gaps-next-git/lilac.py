#!/usr/bin/python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['Airblader'])
    for line in edit_file('PKGBUILD'):
        if 'groups=' in line:
            print(line.replace("'i3' ",'',1))
        else:
            print(line)
