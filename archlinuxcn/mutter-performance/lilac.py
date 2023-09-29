#!/usr/bin/python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['Terence','Saren','Dawdleming'])

    for line in edit_file('PKGBUILD'):
        print (line.replace('groups=(gnome)', ''))
