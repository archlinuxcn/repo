#!/usr/bin/python3

from lilaclib import *

def pre_build():
    aur_pre_build(name='linux-clear', maintainers=['JeremyStarTM'])

    for line in edit_file('PKGBUILD'):
        if line.strip().startswith(': "${_subarch:=""}"'):
            print('_subarch=42') # Generic-x86-64-v3
        elif line.strip().startswith('pkgbase='):
            print('pkgbase=linux-clear-x64-v3')
        elif line.strip().startswith('license='):
            print("license=('GPL-2.0-only')")
        elif line.strip().startswith('_clr='): # Temporarily fix tag typo
            print("_clr=3-1472")
        elif 'more-uarches-for-kernel-' in line.strip(): # Temporarily fix patch filename
            index = line.find('uarches')
            print('{}ISA-levels-and{}'.format(line[:index], line[index:]))
        else:
            print(line)
