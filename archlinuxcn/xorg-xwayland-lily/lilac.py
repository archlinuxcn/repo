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
      line = line.replace(')', "\n            'c1eb92b042befcffe5ba2b0797d2dde4984adf76acbba778eda638d1fab45eac34e2341338cf562460d58d380f768dd40966183e550a29e186f092e8112ab674')")
    elif line.startswith('groups='):
      continue
    print(line)

def post_build():
  git_add_files(g.files)
  git_commit()
