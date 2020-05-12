# Maintainer: Graeme Gott <graeme@gottcode.org>

pkgname=gottet
pkgver=1.1.9
pkgrel=1
pkgdesc='A tetris clone using the Qt GUI toolkit'
arch=('i686' 'x86_64')
url="https://gottcode.org/$pkgname/"
license=('GPL3')
depends=('qt5-base')
makedepends=('qt5-tools')
source=("https://gottcode.org/$pkgname/$pkgname-$pkgver-src.tar.bz2")
sha256sums=('6c979caa5b3fa6854ca8367ca0595814fcc101f0bdfad02d64219dd9049abb2b')

build() {
  cd "$pkgname-$pkgver"

  qmake-qt5 PREFIX=/usr
  make
}

package() {
  cd "$pkgname-$pkgver"

  make INSTALL_ROOT="$pkgdir/" install
}
