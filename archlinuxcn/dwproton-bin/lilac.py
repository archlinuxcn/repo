#!/usr/bin/env python3
from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['shira'])
    for line in edit_file('PKGBUILD'):
        line: str
        if line.startswith('depends_x86_64='):
            print('makedepends=(nvidia-utils)')
        print(line)
