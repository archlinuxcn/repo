#!/usr/bin/env python3
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

from lilaclib import *

build_prefix = 'extra-x86_64'

def pre_build():
    aur_pre_build()

    for line in edit_file('PKGBUILD'):
        print(line)
        if line.strip().startswith('makedepends='):
            print('makedepends+=("git" "python2" "node-gyp")') # Should depend on git


post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)


