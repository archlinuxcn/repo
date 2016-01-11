#!/usr/bin/env python3
#
# This is a complex version of lilac.py for building
# a package from AUR.
#
# You can do something before/after building a package,
# including modify the 'pkgver' and 'md5sum' in PKBUILD.
#
# This is especially useful when a AUR package is
# out-of-date and you want to build a new one, or you
# want to build a package directly from sourceforge but
# using PKGBUILD from AUR.
#
# See also:
# [1] ruby-sass/lilac.py
# [2] aufs3-util-lily-git/lilac.py
# [3] octave-general/lilac.py
#

from lilaclib import *

build_prefix = 'extra-x86_64'

def pre_build():
    aur_pre_build()

    # redownload binary package everytime
    for line in edit_file('PKGBUILD'):
        # edit PKGBUILD
        if line.strip().startswith("PKGEXT"):
            continue
        if line.strip().startswith("'9c752be551429c6ce5946d4fcae24464'"):
            line = " 'a585d6a76f47f9accdf090379ecb6d1f') "
        print(line)

    for line in edit_file("atom-python.patch"):
        if line.strip().startswith("+unset"):
            line = "+ "
        if line.strip().startswith("+Exec=env"):
            line = "+Exec=env PYTHON=python2 /usr/share/atom/atom %U"
        print(line)


post_build = aur_post_build

# do some cleanup here after building the package, regardless of result
# def post_build_always(success):
#   pass

if __name__ == '__main__':
    single_main(build_prefix)
