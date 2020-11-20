#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build()
    for line in edit_file('PKGBUILD'):
        if line.startswith('prepare()'):
            print('_' + line)
        elif line.startswith('pkgver()'):
            print(line)
            print('  _prepare 1>&2')
        else:
            print(line)
    vcs_update()

def post_build():
    aur_post_build()
