from types import SimpleNamespace

from lilaclib import *

g = SimpleNamespace()

def pre_build():
  g.files = download_official_pkgbuild('xorg-xwayland')

  for line in edit_file('PKGBUILD'):
    if line.startswith('pkgname='):
      line = 'pkgname=xorg-xwayland-lily'
    if line.startswith('pkgdesc='):
      line = line[:-1] + ', with !733 HiDPI patch"'
    elif line.startswith('provides'):
      line = "provides=('xorg-server-xwayland' 'xorg-xwayland' 'xorg-xwayland-hidpi-xprop')"
    elif line.startswith('conflicts'):
      line = "conflicts=('xorg-server-xwayland' 'xorg-xwayland')"
    elif line.startswith('validpgpkeys='):
      line += '''
prepare() {
  cd "${srcdir}/xwayland-$pkgver"
  patch -Np1 < ../hidpi.patch
}'''
    elif line.startswith('source=('):
      line = line.replace(')', ' hidpi.patch)')
    elif "'SKIP'" in line:
      line = line.replace(')', '\n            16ccf43bdde029c21d9733cb65809f242a6d95111d03d72a7263e0aca2810a12507ed95b83320c5ed7a2b96bdde044aa57f218e20731a4e2e96f888a087271fd)')
    elif line.startswith('groups='):
      continue
    print(line)

def post_build():
  git_add_files(g.files)
  git_commit()
