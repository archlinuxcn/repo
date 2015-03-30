#!/usr/bin/env python3

from lilaclib import *

build_prefix = 'extra-x86_64'
post_build = aur_post_build

def pre_build():
    aur_pre_build()
    for l in edit_file('PKGBUILD'):
        l = l.rstrip('\n')
        if l.startswith('provides='):
            l = 'provides=("$_pkgname")'
        elif l.startswith('conflicts='):
            l = 'conflicts=("$_pkgname")'
        print(l)
    vcs_update()

if __name__ == '__main__':
  single_main()
