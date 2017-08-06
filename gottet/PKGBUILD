# Maintainer: Graeme Gott <graeme@gottcode.org>

pkgname=gottet
pkgver=1.1.4
pkgrel=1
pkgdesc='A tetris clone using the Qt GUI toolkit'
arch=('i686' 'x86_64')
url="https://gottcode.org/$pkgname/"
license=('GPL3')
depends=('qt5-base')
makedepends=('qt5-tools')
source=("https://gottcode.org/$pkgname/$pkgname-$pkgver-src.tar.bz2")
sha256sums=('f5aeb5cd260b0798c6a3a7cf018c67977be7a475085aa9cf0ca51e0e61d8ddac')

build() {
  cd "$pkgname-$pkgver"

  qmake-qt5 PREFIX=/usr
  make
}

package() {
  cd "$pkgname-$pkgver"

  make INSTALL_ROOT="$pkgdir/" install
}
