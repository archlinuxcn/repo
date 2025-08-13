#!/usr/bin/env python3

from types import SimpleNamespace

from lilaclib import *

g = SimpleNamespace()

def pre_build():
  g.files = download_official_pkgbuild('symengine')

  for line in edit_file('PKGBUILD'):
    line = line.replace('$pkgname', 'symengine')
    line = line.replace('${pkgname}', 'symengine')
    line = line.replace('WITH_TCMALLOC=ON', 'WITH_TCMALLOC=OFF')
    if line.startswith('arch='):
      line = 'arch=(aarch64 x86_64)'
    if line.startswith('pkgname='):
      line = 'pkgname=symengine-notcmalloc'
    if line.startswith('package()'):
      print(line)
      print('  provides+=(symengine=$pkgver)')
      print('  conflicts+=(symengine=$pkgver)')
      continue
    print(line)

def post_build():
  git_add_files([f for f in g.files if not f.startswith(".")])
  git_commit()
