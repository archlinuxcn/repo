#!/usr/bin/python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['petronny', 'AutoUpdateBot'])
    for line in edit_file('PKGBUILD'):
        print(line.replace('gcc-14', 'gcc').replace('g++-14', 'g++'))
