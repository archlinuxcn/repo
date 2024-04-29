#!/usr/bin/python

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['daizhirui'])

    for line in edit_file('PKGBUILD'):
        if not (line.strip().startswith("replaces=('sip")):
            print (line)
