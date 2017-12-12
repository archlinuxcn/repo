#!/usr/bin/env python3
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

from lilaclib import *

depends = ["dee", "gyp-git", "range-v3"]

build_prefix = 'extra-x86_64'

def pre_build():
    aur_pre_build()
    for line in edit_file('PKGBUILD'):
        if line.startswith("makedepends=("):
            line = "makedepends=('cmake' 'git' 'gyp-git' 'libexif' 'libva' 'libwebp' 'mtdev' 'range-v3' 'python' 'python2' 'gtk3' 'libappindicator-gtk3' 'dee' 'libappindicator-gtk2')"
        print(line)

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)


