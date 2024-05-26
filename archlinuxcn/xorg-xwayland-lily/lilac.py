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
      line = line.replace(')', "\n            '4ac0347b5e75b1e165a85a5921dba34ac4fd5fe63f579018250bf90197fdcd32c7af24bb498d1020f031f2d6132457e1f0396c657b386f26fcf65042bc5b20e0')")
    elif line.startswith('groups='):
      continue
    print(line)

def post_build():
  git_add_files(g.files)
  git_commit()
