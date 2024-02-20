#!/usr/bin/env python3

from types import SimpleNamespace

from lilaclib import *

g = SimpleNamespace()

def pre_build():
  g.files = download_official_pkgbuild('gperftools')

  for line in edit_file('PKGBUILD'):
    line = line.replace('$pkgname', 'gperftools')
    line = line.replace('${pkgname}', 'gperftools')
    if line.startswith('arch='):
      line = 'arch=(aarch64 x86_64)'
    if line.startswith('pkgname='):
      line = 'pkgname=gperftools-dynamic-tls'
    if line.startswith('build()'):
      print("""prepare() {
  cd gperftools-$pkgver
  find -type f -exec sed -i -e 's/ABSL_ATTRIBUTE_INITIAL_EXEC//g' {} \;
}
""")
    if line.startswith('package()'):
      print(line)
      print('  provides+=(gperftools=$pkgver)')
      print('  conflicts+=(gperftools=$pkgver)')
      continue
    print(line)

def post_build():
  git_add_files([f for f in g.files if not f.startswith(".")])
  git_commit()
