# Maintainer: codestation <codestation404 at gmail dot com>

pkgname=wxmedit
pkgver=3.1
pkgrel=1
pkgdesc="Cross-platform Text/Hex Editor, a fork of MadEdit with bug fixes and improvements"
arch=("i686" "x86_64")
url="https://wxmedit.github.io/"
license=('GPL')
depends=('wxgtk2.8' 'icu' 'desktop-file-utils')
makedepends=('boost')
source=("http://downloads.sourceforge.net/project/$pkgname/$pkgver/wxMEdit-$pkgver.tar.gz")
install=wxmedit.install
sha256sums=('6060270fb01efb6cefeb83772202d8682675ec6b80cbb1e03f54f486e3bdb1d5')

build() {
  cd "$srcdir/wxMEdit-$pkgver"

  ./configure --prefix=/usr --with-wx-config=/usr/bin/wx-config-2.8
  make
}

package() {
  cd "$srcdir/wxMEdit-$pkgver"
  make DESTDIR="${pkgdir}" install
}
