#!/usr/bin/env python3
from lilaclib import *

build_prefix = 'extra-x86_64'

def pre_build():
  # obtain base PKGBUILD, e.g.
  download_official_pkgbuild('pygtk')

  for line in edit_file('PKGBUILD'):
    # edit PKGBUILD
    if 'pkgname=pygtk' in line:
        print('pkgname=deepin-pygtk')
        print('_'+line)
    elif 'pkgdesc' in line:
        print('pkgdesc="Python bindings for the GTK widget set - with patches to fix memory leak for deepin-ui"')
    elif 'optdepends=' in line:
        print(line)
        print('provides=("pygtk=$pkgver")')
        print('conflicts=("pygtk")')
    elif 'source=' in line:
        print(line.replace("${pkgname}","$_pkgname"))
        print('        10_fix_create_layout_unref.patch')
    elif 'sha256sums=' in line:
        print(line)
        print("            '283836d6fe8eda2a1bd32f551b2677e1b9e6e3cee8e48e6c4b861375810d8712'")
    elif 'patch -Np1 -i' in line:
        print(line)
        print("  patch -Np1 -i \"${srcdir}/10_fix_create_layout_unref.patch\"")
    elif 'cd "${srcdir}/${pkgname}-${pkgver}"' in line:
        print(line.replace("${pkgname}","$_pkgname"))
    else:
        print(line)

def post_build():
  # do something after the package has successfully been built
  git_add_files('PKGBUILD')
  git_add_files('10_fix_create_layout_unref.patch')
  git_commit()

# do some cleanup here after building the package, regardless of result
# def post_build_always(success):
#   pass

if __name__ == '__main__':
  single_main()
