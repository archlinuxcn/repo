#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build('baka-mplayer-git', maintainers=['u8sand'])
    for line in edit_file('PKGBUILD'):
        if line.startswith('replaces='):
            continue

        print(line)
