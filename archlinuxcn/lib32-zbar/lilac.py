#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build()
    add_depends(['libdbus-1.so', 'libjpeg.so'])
    add_provides(['libzbar.so'])
    pattern = re.compile("['\"]?lib32-imagemagick['\"]? ?")
    for line in edit_file('PKGBUILD'):
        if line.startswith('depends='):
            print(pattern.sub('', line))
        elif line.strip().startswith('./configure '):
            print(line + ' --without-imagemagick')
        else:
            print(line)


def post_build():
    aur_post_build()
