#!/usr/bin/env python3
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

from lilaclib import *

build_prefix = 'extra-x86_64'
post_build = aur_post_build

def pre_build():
    aur_pre_build()
    for line in edit_file('PKGBUILD'):
        if line.strip() == 'source_x86_64=("http://dl.google.com/linux/direct/${pkgname}_current_amd64.deb")':
            line = 'source_x86_64=("${pkgname}_${pkgver}_amd64.deb::http://dl.google.com/linux/direct/>${pkgname}_current_amd64.deb")'
        print(line)
    run_cmd(['updpkgsums'])

if __name__ == '__main__':
  single_main(build_prefix)
