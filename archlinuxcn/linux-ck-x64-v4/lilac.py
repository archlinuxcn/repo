#!/usr/bin/python3

from lilaclib import *

def pre_build():
    aur_pre_build(name='linux-ck', maintainers=['graysky'])

    for line in edit_file('PKGBUILD'):
        if line.strip().startswith('_subarch='):
            print('_subarch=42') # Generic-x86-64-v4
        elif line.strip().startswith('pkgbase='):
            print('pkgbase=linux-ck-x64-v4')
        elif line.strip().startswith('license='):
            print("license=('GPL-2.0-only')")
        else:
            print(line)
