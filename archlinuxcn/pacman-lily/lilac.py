from types import SimpleNamespace

from lilaclib import *

g = SimpleNamespace()

def pre_build():
  g.files = download_official_pkgbuild('pacman')

  build = False
  package = False
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
      line = line.replace('(', '(pacman.patch\n        pacman-syncdb\n        ')
    elif line.startswith('sha256sums=('):
      line = line.replace('(', '(61e0b85dadb341ea14e5aa28b0b1edf98871bc3dffd1083fb5775fc28a65e113\n            207d5cee261bba18e650bbd2c249ffd8fe9c1dbd7de6b241d8bf011848faa70b\n            ')
    elif line.startswith('package() '):
      package = True
    elif package and line.startswith('}'):
      line = '  install -m755 "$srcdir/pacman-syncdb" "$pkgdir/usr/bin"\n' + line
      package = False

    if '$pkgname' in line:
      line = line.replace('$pkgname', 'pacman')
    print(line)

def post_build():
  git_add_files(g.files)
  git_commit()
