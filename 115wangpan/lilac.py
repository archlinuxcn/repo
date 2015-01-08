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
# depends = []

def pre_build():
  # obtain base PKGBUILD, e.g.
  aur_pre_build()

  for line in edit_file('PKGBUILD'):
    # edit PKGBUILD
    if 'arch=' in line:
        line='arch=(\'x86_64\' \'i686\')'
    elif 'depends=' in line:
        print('if test "$CARCH" == x86_64; then')
        print('\tdepends=(\'lib32-libx11\' \'lib32-gcc-libs\')')
        print('elif test "$CARCH" == i686; then')
        print('\tdepends=(\'libx11\')')
        line='fi'
    elif 'package()' in line:
        print('build(){')
        print('\tcd ${srcdir}')
        print('\ttar xvf data.tar.gz')
        print('}\n')
        print(line)
        print('\tinstall -dm755 "${pkgdir}/usr/lib"')
        print('\tcp -r "${srcdir}/lib/fonts" "${pkgdir}/usr/lib"')
        print('\tinstall -dm755 "${pkgdir}/usr/share/115wangpan"')
        print('\tinstall -Dm755 "${srcdir}/usr/bin/115pan" "${srcdir}/usr/bin/qt.conf" "${pkgdir}/usr/share/115wangpan"')
        print('\tinstall -dm755  "$pkgdir/usr/bin/"')
        print('\tln -s /usr/share/115wangpan/115pan "${pkgdir}/usr/bin/115pan"')
        print('}')
        break
    print(line)

def post_build():
  # do something after the package has successfully been built
  aur_post_build()

# do some cleanup here after building the package, regardless of result
# def post_build_always(success):
#   pass

if __name__ == '__main__':
  single_main()
