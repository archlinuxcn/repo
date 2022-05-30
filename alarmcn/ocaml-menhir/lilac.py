#!/usr/bin/env python3
#
from lilaclib import *

#build_prefix = 'extra-x86_64'


def pre_build():
    aur_pre_build(maintainers=['soimort', 'xuanruiqi'])

    for line in edit_file('PKGBUILD'):
        # edit PKGBUILD
        if line.strip().startswith("arch="):
            line = 'arch=(x86_64 armv7h aarch64)"'
        print(line)
