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
      line = "provides=('xorg-server-xwayland' 'xorg-xwayland')"
    elif line.startswith('conflicts'):
      line = "conflicts=('xorg-server-xwayland' 'xorg-xwayland')"
    elif line.startswith('validpgpkeys='):
      line += '''
options=('debug' 'strip')

prepare() {
  cd "${srcdir}/xwayland-$pkgver"
  patch -Np1 < ../hidpi.patch
}'''
    elif line.startswith('source=('):
      line = line.replace(')', ' hidpi.patch)')
    elif "'SKIP'" in line:
      line = line.replace(')', '\n            7132c44d9bbf1c5f93906ef301a6e946f0909da0b9273f397281e681ad0da77d62b960a9dd0a640c7209548192fefba9bde03c493f3a89d08cd73a12844bb518)')
    elif line.startswith('groups='):
      continue
    print(line)

def post_build():
  git_add_files(g.files)
  git_commit()
