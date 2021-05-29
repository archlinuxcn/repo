#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers='oxalin')
    in_split = False
    for line in edit_file('PKGBUILD'):
        if line.startswith('package_lib32-libvmaf()'):
            in_split = True
        elif line == '}':
            in_split = False
        if in_split and line.strip().startswith('provides='):
            pos = line.find('(') + 1
            print(f'{line[:pos]}libvmaf.so {line[pos:]}')
        else:
            print(line)

def post_build():
    check_library_provides()
    aur_post_build()
