# Maintainer: Allen Hoffmeyer <allen dot hoffmeyer at gmail dot com>
#               (adapted from work by Louis R. Marascio <lrm at fitnr dot com>)
# Contributor: trader <trader9 at gawab dot com>
# Contributor: masutu <masutu dot arch at googlemail dot com>

pkgname=quantlib
_pkgname=QuantLib
pkgver=1.5
pkgrel=1
pkgdesc="A free/open-source library for quantitative finance."
arch=('i686' 'x86_64')
url="http://quantlib.org"
license=('BSD')
options=(!libtool)
depends=('boost-libs' 'sh')
makedepends=('make' 'boost' 'gcc')
source=(http://downloads.sourceforge.net/project/$pkgname/$_pkgname/$pkgver/$_pkgname-$pkgver.tar.gz)
md5sums=('8dd8d74cfe5c9dafc554b18830b34855')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  ./configure --prefix=/usr
  make 
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  make DESTDIR="$pkgdir/" install
  install -D -m644 LICENSE.TXT $pkgdir/usr/share/licenses/$pkgname/LICENSE.TXT
}

# vim:set ts=2 sw=2 et:
