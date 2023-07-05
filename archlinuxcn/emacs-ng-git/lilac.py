#!/usr/bin/python3

from lilaclib import *

def pre_build(): 
    aur_pre_build(maintainers=['FabioLolix'])

    for line in edit_file('PKGBUILD'):
        if not (line.strip().endswith('pdf')):
            print(line)
