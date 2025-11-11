#!/usr/bin/env python3
from lilaclib import *

def pre_build():
    aur_pre_build('qt5-remoteobjects', maintainers=['arojas'])

    for line in edit_file('PKGBUILD'):

        if line.startswith('groups='):
            continue

        print(line)
