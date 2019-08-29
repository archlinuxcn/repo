# Maintainer: Graeme Gott <graeme@gottcode.org>

pkgname=gottet
pkgver=1.1.8
pkgrel=1
pkgdesc='A tetris clone using the Qt GUI toolkit'
arch=('i686' 'x86_64')
url="https://gottcode.org/$pkgname/"
license=('GPL3')
depends=('qt5-base')
makedepends=('qt5-tools')
source=("https://gottcode.org/$pkgname/$pkgname-$pkgver-src.tar.bz2")
sha256sums=('440e9570e2909e3029cced304774a15d83b4019925ac9a4cfb44c1f8a77592d8')

build() {
  cd "$pkgname-$pkgver"

  qmake-qt5 PREFIX=/usr
  make
}

package() {
  cd "$pkgname-$pkgver"

  make INSTALL_ROOT="$pkgdir/" install
}
