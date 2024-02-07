# Maintainer: Michał Wojdyła < micwoj9292 at gmail dot com >
# Contributor: Stefan Husmann <stefan-husmann@t-online.de>
# Contributor: Sergej Pupykin <pupykin.s+arch@gmail.com>
# Contributor: William Rea <sillywilly@gmail.com>

pkgname=xrestop
pkgver=0.6
pkgrel=2
pkgdesc="Uses the X-Resource extension to provide 'top' like statistics"
arch=('x86_64')
url="http://freedesktop.org/wiki/Software/xrestop"
license=('GPL-2.0-or-later')
depends=('libxres' 'ncurses')
source=(https://xorg.freedesktop.org/archive/individual/app/$pkgname-$pkgver.tar.gz)
md5sums=('1c11bc50190bdc6091bc72ed2991300f')

build() {
  cd $pkgname-$pkgver
  ./configure --prefix=/usr --mandir=/usr/share/man
  make
}

package() {
  cd $pkgname-$pkgver
  make DESTDIR="$pkgdir" install
}
