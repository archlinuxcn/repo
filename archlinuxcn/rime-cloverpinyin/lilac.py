#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build()
    for line in edit_file('PKGBUILD'):
        if line.startswith('pkgdesc'):
            line = 'pkgdesc="Clover Simplified pinyin input for rime"'
        print(line)
