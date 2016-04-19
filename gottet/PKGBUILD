# Maintainer: Graeme Gott <graeme@gottcode.org>

pkgname=gottet
pkgver=1.1.1
pkgrel=1
pkgdesc='A tetris clone using the Qt GUI toolkit'
arch=('i686' 'x86_64')
url="http://gottcode.org/$pkgname/"
license=('GPL3')
depends=('qt5-base')
install="$pkgname.install"
source=("http://gottcode.org/$pkgname/$pkgname-$pkgver-src.tar.bz2")
sha256sums=('c276dba1f7d145d74713fdc92fe2b22cf538ace0115026466109857f7b543163')

build() {
  cd "$pkgname-$pkgver"

  qmake-qt5 PREFIX=/usr
  make
}

package() {
  cd "$pkgname-$pkgver"

  make INSTALL_ROOT="$pkgdir/" install
}
