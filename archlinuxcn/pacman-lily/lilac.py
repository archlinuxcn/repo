from types import SimpleNamespace

from lilaclib import *

g = SimpleNamespace()

def pre_build():
  g.files = download_official_pkgbuild('pacman')

  build = False
  for line in edit_file('PKGBUILD'):
    if line.startswith('pkgname='):
      line = 'pkgname=pacman-lily'
    elif line.startswith('pkgdesc='):
      line = line[:-1] + ' (no disabling-server-on-error)"'
    elif line.startswith('provides=('):
      line = line.replace(')', ' "pacman=$pkgver")\n') + "conflicts=('pacman')"
    elif line.startswith('build() '):
      build = True
    elif line.startswith('groups=('):
      continue
    elif build and line.startswith('  cd '):
      line += '\n  patch -p1 -i "${srcdir}/pacman.patch"'
      build = False
    elif line.startswith('source=('):
      line = line.replace('(', '(pacman.patch\n        ')
    elif line.startswith('sha256sums=('):
      line = line.replace('(', '(b8fa45a99dfb5b902aae6376043f6f90806bb8e6e32e969b5160fc7d452dd898\n            ')
    if '${pkgname}' in line:
      line = line.replace('${pkgname}', 'pacman-lily')
    print(line)

def post_build():
  git_add_files(g.files)
  git_commit()
