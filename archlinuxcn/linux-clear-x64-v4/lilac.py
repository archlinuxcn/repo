#!/usr/bin/python3

from lilaclib import *

def pre_build():
    aur_pre_build()
    for line in edit_file('PKGBUILD'):
        if line.strip().startswith('_subarch'):
            print('_subarch=39') # Generic-x86-64-v4
        elif line.strip().startswith('_localmodcfg'):
            print('_localmodcfg=y')
        else:
            print(line)
