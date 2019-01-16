# $Id: PKGBUILD 114533 2014-07-01 19:33:20Z jelle $
# Contributor: Sergej Pupykin <pupykin.s+arch@gmail.com>
# Contributor: William Rea <sillywilly@gmail.com>
# Maintainer: zoe <chp32 [at] gmail [dot] com>

pkgname=goocanvas1
pkgver=1.0.0
pkgrel=5
pkgdesc="A cairo canvas widget for GTK+"
arch=(i686 x86_64)
url="http://live.gnome.org/GooCanvas"
options=('docs')
license=("LGPL")
makedepends=('python')
depends=('gtk2')
source=(http://ftp.gnome.org/pub/GNOME/sources/goocanvas/1.0/goocanvas-$pkgver.tar.bz2)
sha256sums=('1c072ef88567cad241fb4addee26e9bd96741b1503ff736d1c152fa6d865711e')

build() {
  cd $srcdir/goocanvas-$pkgver
  ./configure --prefix=/usr --disable-static
  make
}

package() {
  cd $srcdir/goocanvas-$pkgver
  make DESTDIR=$pkgdir install
}
check() {
  cd $srcdir/goocanvas-$pkgver
  make check
}
