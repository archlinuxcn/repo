#!/usr/bin/python3

from lilaclib import *

def pre_build():
    aur_pre_build(name='linux-clear', maintainers=['JeremyStarTM'])

    for line in edit_file('PKGBUILD'):
        if line.strip().startswith(': "${_subarch:=""}"'):
            print('_subarch=42') # Generic-x86-64-v3
        elif line.strip().startswith('pkgbase='):
            print('pkgbase=linux-clear-x64-v3')
        else:
            print(line)
