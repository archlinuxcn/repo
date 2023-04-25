#!/usr/bin/python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['gcala'])
    add_depends(['futuresql-git'])

    for line in edit_file('PKGBUILD'):
        line = line.replace("'fakeroot'", "")
        line = line.replace("'binutils'", "")
        print (line)
