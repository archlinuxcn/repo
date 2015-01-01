# Maintainer: codestation <codestation404 at gmail dot com>

pkgname=wxmedit
pkgver=2.9.9
pkgrel=1
pkgdesc="Cross-platform Text/Hex Editor, a fork of MadEdit with bug fixes and improvements"
arch=("i686" "x86_64")
url="https://wxmedit.github.io/"
license=('GPL')
depends=('wxgtk2.8' 'icu' 'desktop-file-utils' 'boost')
source=("http://downloads.sourceforge.net/project/$pkgname/$pkgver/wxMEdit-$pkgver.tar.gz")
install=wxmedit.install
md5sums=('b718c9a2f35e3435aa90392653b30853')

build() {
  cd "$srcdir/wxMEdit-$pkgver"

  ./configure --prefix=/usr --with-wx-config=/usr/bin/wx-config-2.8
  make
}

package() {
  cd "$srcdir/wxMEdit-$pkgver"
  make DESTDIR="${pkgdir}" install
}
