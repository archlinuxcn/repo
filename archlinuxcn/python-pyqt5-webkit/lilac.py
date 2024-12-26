#!/usr/bin/env python3
from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['zen', 'arojas', 'Universebenzene'])
    for line in edit_file('PKGBUILD'):
        if "groups=" in line:
            line = ""
        print(line)
