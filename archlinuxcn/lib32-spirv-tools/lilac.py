#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build()
    for line in edit_file('PKGBUILD'):
        if not line.startswith('groups='):
            print(line)

def post_build():
    aur_post_build()
