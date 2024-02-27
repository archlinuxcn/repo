#!/usr/bin/python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['taotieren','Ataraxy','severach'])

    for line in edit_file('PKGBUILD'):
        if line.startswith('license='):
            line = "license=('AGPL-3.0-or-later')"
        print(line)

        if line.strip().startswith('pkgrel='):
            print('epoch=1')
