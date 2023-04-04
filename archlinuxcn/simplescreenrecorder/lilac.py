#!/usr/bin/python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['arojas','FredBezies'])

    for line in edit_file('PKGBUILD'):
        if not (line.startswith('install=')):
            print (line)
