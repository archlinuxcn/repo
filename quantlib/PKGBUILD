# Maintainer: Allen Hoffmeyer <allen dot hoffmeyer at gmail dot com>
#               (adapted from work by Louis R. Marascio <lrm at fitnr dot com>)
# Contributor: trader <trader9 at gawab dot com>
# Contributor: masutu <masutu dot arch at googlemail dot com>
# Contributor: Guillaume Horel <guillaume.horel@gmail.com>

pkgname=quantlib
_pkgname=QuantLib
pkgver=1.10.1
pkgrel=1
pkgdesc="A free/open-source library for quantitative finance."
arch=('i686' 'x86_64')
url="http://quantlib.org"
license=('BSD')
options=(!libtool)
depends=('boost-libs' 'sh')
makedepends=('make' 'boost' 'gcc')
source=(http://downloads.sourceforge.net/project/$pkgname/$_pkgname/$pkgver/$_pkgname-$pkgver.tar.gz)
sha256sums=('bcb88be6a485ae62bb00027c180294d2af0dbea252e4f76e1284e4af3a9c4432')

build() {
  cd "$srcdir"/"$_pkgname-$pkgver"/
  ./autogen.sh
  ./configure --prefix=/usr --enable-intraday --enable-openmp --disable-static
  make
}

package() {
  cd "$srcdir"/"$_pkgname-$pkgver"/
  make DESTDIR="$pkgdir/" install
  install -D -m644 LICENSE.TXT "$pkgdir/usr/share/licenses/$pkgname/LICENSE.TXT"
}

# vim:set ts=2 sw=2 et:
