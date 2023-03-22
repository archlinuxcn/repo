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
options=('debug' 'strip')

prepare() {
  cd "${srcdir}/xwayland-$pkgver"
  patch -Np1 < ../hidpi.patch
}'''
    elif line.startswith('source=('):
      line = line.replace(')', ' hidpi.patch)')
    elif "'SKIP'" in line:
      line = line.replace(')', '\n            2e16d1e3222b02d27a544c8df5132cf22c7fd0601c3a967a603cf2e14b7154ac1d3d6e4ea66e0bf4086f9f18fe0bc2428653ecbd8b23a0e90c3f0a9b1ecf36d9)')
    elif line.startswith('groups='):
      continue
    print(line)

def post_build():
  git_add_files(g.files)
  git_commit()
