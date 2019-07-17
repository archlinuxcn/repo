# Maintainer: Antonio Rojas <arojas@archlinux.org>

pkgname=plasma5-applets-window-buttons
pkgver=0.5.0
pkgrel=1
pkgdesc="Plasma 5 applet in order to show window buttons in your panels"
arch=(x86_64)
url="https://github.com/psifidotos/applet-window-buttons"
license=(GPL)
depends=(plasma-workspace)
makedepends=(extra-cmake-modules)
source=($pkgname-$pkgver.tar.gz::"https://github.com/psifidotos/applet-window-buttons/archive/v$pkgver.tar.gz")
sha256sums=('918237d57d26c1f700ba85ee401d90fafe46888832e85604abba61846012bf2d')

prepare() {
  mkdir -p build
}

build() {
  cd build
  cmake ../applet-window-buttons-$pkgver \
    -DCMAKE_INSTALL_PREFIX=/usr
}

package() {
  cd build
  make DESTDIR="$pkgdir" install
}
