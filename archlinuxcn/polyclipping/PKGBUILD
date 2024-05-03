# Maintainer: Jelle van der Waa <jelle@archlinux.org>

pkgname=polyclipping
pkgver=6.4.2
pkgrel=4
pkgdesc="Polygon clipping library"
arch=('x86_64')
url="https://sourceforge.net/projects/polyclipping/"
license=('Boost')
depends=('gcc-libs')
makedepends=('cmake')
source=("https://downloads.sourceforge.net/polyclipping/clipper_ver${pkgver}.zip")
sha256sums=('a14320d82194807c4480ce59c98aa71cd4175a5156645c4e2b3edd330b930627')

build() {
  cd "${srcdir}"
  mkdir -p build && cd build
  cmake -DCMAKE_INSTALL_PREFIX=/usr -DVERSION=$pkgver ../cpp
  make
}

package() {
  cd "${srcdir}/build"
  make install DESTDIR="$pkgdir"
  install -d "$pkgdir/usr/share/licenses/$pkgname"
}
