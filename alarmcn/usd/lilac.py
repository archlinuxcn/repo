#!/usr/bin/env python3

from types import SimpleNamespace

from lilaclib import *

g = SimpleNamespace()

def pre_build():
  g.files = download_official_pkgbuild('usd')

  for line in edit_file('PKGBUILD'):
    if line.startswith('arch='):
      line = 'arch=(aarch64 x86_64)'
    if line.startswith('makedepends='):
      line = line.replace(' cuda', '')
    if line.startswith('prepare()'):
      print('source+=(0001-Use-Valgrind-macro-to-mark-memory-defined.patch)')
      print("""prepare() {
  (cd OpenUSD
  patch -Np1 -i "$srcdir/0001-Use-Valgrind-macro-to-mark-memory-defined.patch")
  _prepare
}
""")
      print(f"_{line}")
      continue
    print(line)
  run_cmd(['updpkgsums'])

def post_build():
  git_add_files([f for f in g.files if not f.startswith(".")])
  git_commit()
