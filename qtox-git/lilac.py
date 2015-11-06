#!/usr/bin/env python3

from lilaclib import *

depends = ['libfilteraudio-git']

build_prefix = 'extra-x86_64'
post_build = aur_post_build

def pre_build():
    aur_pre_build()
    for line in edit_file('PKGBUILD'):
        if line.strip().startswith('source=('):
            line='source=("$_pkgname::git+https://github.com/tux3/qTox.git#branch=newav_final_for_realsies")'
        print(line)


if __name__ == '__main__':
  single_main()
