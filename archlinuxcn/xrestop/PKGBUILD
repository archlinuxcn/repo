# Contributor: Sergej Pupykin <pupykin.s+arch@gmail.com>
# Contributor: William Rea <sillywilly@gmail.com>
# Maintainer: Stefan Husmann <stefan-husmann@t-online.de>

pkgname=xrestop
pkgver=0.4
pkgrel=7
pkgdesc="Uses the X-Resource extension to provide 'top' like statistics"
arch=('x86_64')
url="http://freedesktop.org/wiki/Software/xrestop"
license=('GPL')
depends=('libxres' 'ncurses')
source=(http://downloads.yoctoproject.org/releases/$pkgname/$pkgname-$pkgver.tar.gz)
md5sums=('d8a54596cbaf037e62b80c4585a3ca9b')

build() {
  cd $pkgname-$pkgver
  ./configure --prefix=/usr --mandir=/usr/share/man
  make
}

package() {
  cd $pkgname-$pkgver
  make DESTDIR="$pkgdir" install
}
