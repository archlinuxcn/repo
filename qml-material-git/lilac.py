#!/usr/bin/env python3
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

from lilaclib import *

build_prefix = 'extra-x86_64'
post_build = aur_post_build

def pre_build():
    # aur_pre_build()

    # hack to change PKGBUILD before run makepkg -od
    if os.path.exists('PKGBUILD'):
      pkgver, pkgrel = get_pkgver_and_pkgrel()
    else:
      pkgver = None

    _g.aur_pre_files = clean_directory()
    if name is None:
      name = os.path.basename(os.getcwd())
    _g.aur_building_files = download_aur_pkgbuild(name)

    new_pkgver = get_pkgver_and_pkgrel()[0]
    if pkgver and pkgver == new_pkgver:
      # change pkgrel to what specified in PKGBUILD
      update_pkgrel(pkgrel)

    # change PKGBUILD
    for line in edit_file('PKGBUILD'):
        # edit PKGBUILD
        if line.strip().startswith("prepare() {"):
            line="build() {"
        print(line)

    if do_vcs_update and name.endswith(('-git', '-hg', '-svn', '-bzr')):
      vcs_update()

if __name__ == '__main__':
    single_main(build_prefix)


