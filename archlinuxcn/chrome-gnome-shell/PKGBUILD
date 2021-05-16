# Maintainer: Bartłomiej Piotrowski <bpiotrowski@archlinux.org>

pkgname=chrome-gnome-shell
pkgver=10.1
pkgrel=5
pkgdesc='Native browser connector for integration with extensions.gnome.org'
arch=(any)
url='https://wiki.gnome.org/Projects/GnomeShellIntegrationForChrome'
license=(GPL)
depends=(gnome-shell python-requests python-gobject)
makedepends=(cmake jq git)
_commit=815ec9e1afa52bd3af5047e176a4ea9c1bfa2514  # tags/v10.1^0
source=(git+https://git.gnome.org/browse/chrome-gnome-shell#commit=$_commit)
md5sums=('SKIP')

pkgver() {
  cd $pkgname
  git describe | sed 's/^v//;s/-/+/g'
}

prepare() {
  cd $pkgname
  mkdir -p build
}

build() {
  cd $pkgname/build
  cmake .. \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_INSTALL_LIBDIR=lib \
    -DBUILD_EXTENSION=OFF
}

package() {
  make -C $pkgname/build DESTDIR="$pkgdir" install
}
