#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers='Askannz')
    pattern = re.compile("['\"]?python-setuptools['\"]? ?")
    for line in edit_file('PKGBUILD'):
        if line.startswith('depends='):
            print(pattern.sub('', line))
        else:
            print(line)

def post_build():
    aur_post_build()
