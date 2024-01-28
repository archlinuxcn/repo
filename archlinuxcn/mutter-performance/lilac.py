#!/usr/bin/python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['Terence','Saren','Dawdleming'])

    for line in edit_file('PKGBUILD'):
        if line.startswith('license='):
            line = "license=('GPL-2.0-or-later')"
        print (line.replace('groups=(gnome)', ''))
