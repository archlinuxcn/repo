#!/usr/bin/env python3
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

from lilaclib import *

depends = ['dee',
           'google-breakpad-git',
           'libunity']

build_prefix = 'extra-x86_64'
post_build = aur_post_build


def pre_build():
    aur_pre_build()

    for line in edit_file('PKGBUILD'):
        # edit PKGBUILD
        if line.strip().startswith('"$srcdir/Libraries/gyp/gyp"'):
            print('export LANG=en_US.UTF-8')
        print(line)

if __name__ == '__main__':
  single_main()
