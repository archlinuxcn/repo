#!/usr/bin/python3
from types import SimpleNamespace

from lilaclib import *

g = SimpleNamespace()

def pre_build():
    g.files = download_official_pkgbuild('mbedtls2')

    for line in edit_file('PKGBUILD'):
        if line.startswith('pkgname='):
            print('pkgname=mbedtls2-cmac')
        elif line.startswith('pkgdesc='):
            line = line[:-1] + ' (with CMAC)'
            print(line)
        elif line.startswith('checkdepends='):
            print(line)
            print('conflicts=(mbedtls2)')
        elif line.startswith('build()'):
            print(line)
            print('scripts/config.py set MBEDTLS_CMAC_C')
        else:
            print(line)

def post_build():
  git_add_files(g.files)
  git_commit()
