#!/usr/bin/python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['taotieren','Ataraxy','severach'])

    in_pkgver = False
    for line in edit_file('PKGBUILD'):
        if line.strip().startswith('pkgrel='):
            print('epoch=1')

        if in_pkgver == False:
            print(line)
        else:
            if line.strip().startswith('}'):
                in_pkgver = False
                print(line)
            continue

        if line.strip().startswith('pkgver()'):
            in_pkgver = True
            print("set -u")
            print("cd \"${srcdir}/${_pkgname}\"")
            print("local _ver")
            print("_ver=\"$(git describe --long --tags | sed -e 's/\([^-]*-g\)/r\\1/' -e 's/-/./g')\"")
            print("_ver=\"${_ver#nightly.}\"")
            print("echo \"${_ver}\"")
            print("set +u")
