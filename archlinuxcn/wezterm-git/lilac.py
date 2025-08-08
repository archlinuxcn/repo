#!/usr/bin/env python3
from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['wez', 'xiota'])

    pkgver = False
    for line in edit_file('PKGBUILD'):

        if line.startswith("pkgver()"):
            print("pkgver() {")
            print('  cd "$srcdir/wezterm" || exit 1')
            print('  git -c "core.abbrev=8" show -s "--format=%cd-%h" "--date=format:%Y%m%d-%H%M%S" | tr - .')
            print('}')
            pkgver = True
        if pkgver:
            if line.strip() == "}":
                pkgver = False
            line = ""

        print(line)
