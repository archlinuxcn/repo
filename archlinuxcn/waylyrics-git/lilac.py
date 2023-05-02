#!/usr/bin/python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['poly000'])

    for line in edit_file('PKGBUILD'):
        print (line)
        if line.strip().startswith('install -Dm644 io.poly000.waylyrics.gschema.xml'):
            print ('    cd -')
