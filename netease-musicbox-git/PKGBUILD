# Maintainer: Jiachen Yang <farseerfc@gmail.com>
pkgname=netease-musicbox-git
_gitname=musicbox
pkgver=r481.c045426
pkgrel=3
pkgdesc="A sexy command line interface musicbox for NetEase based on Python"
arch=(any)
url="https://github.com/darknessomi/musicbox"
license=('MIT')
depends=('python2' 'mpg123' 'python2-beautifulsoup4' 'python2-requests' 'python2-setuptools' 'python2-crypto' 'python2-future')
optdepends=('aria2: music caching'
            'python2-keybinder2: global keybindings'
            'libnotify: notifications'
            'python2-pyqt4: lyrics support'
            'python2-dbus: lyrics support'
           )
makedepends=('git')
options=(!emptydirs)
source=("git+https://github.com/darknessomi/musicbox")
sha256sums=('SKIP')
provides=('netease-musicbox')
conflicts=('netease-musicbox')
install=$pkgname.install

pkgver() {
  cd $_gitname
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

package() {
  cd "$srcdir/$_gitname"
  python2 setup.py install --root="$pkgdir/" --optimize=1
  mkdir -p "${pkgdir}/usr/share/licenses/${pkgname}"
  install -m755 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/"
}

# vim:set ts=2 sw=2 et:
