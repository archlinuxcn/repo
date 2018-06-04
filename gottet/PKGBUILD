# Maintainer: Graeme Gott <graeme@gottcode.org>

pkgname=gottet
pkgver=1.1.6
pkgrel=1
pkgdesc='A tetris clone using the Qt GUI toolkit'
arch=('i686' 'x86_64')
url="https://gottcode.org/$pkgname/"
license=('GPL3')
depends=('qt5-base')
makedepends=('qt5-tools')
source=("https://gottcode.org/$pkgname/$pkgname-$pkgver-src.tar.bz2")
sha256sums=('b7124832e4ffdb404e9fd6f6f35ec37eb86352f49dc315fa48aa06aecd3d6c5c')

build() {
  cd "$pkgname-$pkgver"

  qmake-qt5 PREFIX=/usr
  make
}

package() {
  cd "$pkgname-$pkgver"

  make INSTALL_ROOT="$pkgdir/" install
}
