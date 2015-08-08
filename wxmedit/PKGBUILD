# Maintainer: codestation <codestation404 at gmail dot com>

pkgname=wxmedit
pkgver=3.0
pkgrel=1
pkgdesc="Cross-platform Text/Hex Editor, a fork of MadEdit with bug fixes and improvements"
arch=("i686" "x86_64")
url="https://wxmedit.github.io/"
license=('GPL')
depends=('wxgtk2.8' 'icu' 'desktop-file-utils' 'boost')
source=("http://downloads.sourceforge.net/project/$pkgname/$pkgver/wxMEdit-$pkgver.tar.gz")
install=wxmedit.install
sha256sums=('528022fe142e5fcdc54898620d6ebfc2b92a8db059aba2dbeeff97bcb0736ddd')

build() {
  cd "$srcdir/wxMEdit-$pkgver"

  ./configure --prefix=/usr --with-wx-config=/usr/bin/wx-config-2.8
  make
}

package() {
  cd "$srcdir/wxMEdit-$pkgver"
  make DESTDIR="${pkgdir}" install
}
