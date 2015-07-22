# Maintainer: Allen Hoffmeyer <allen dot hoffmeyer at gmail dot com>
#               (adapted from work by Louis R. Marascio <lrm at fitnr dot com>)
# Contributor: trader <trader9 at gawab dot com>
# Contributor: masutu <masutu dot arch at googlemail dot com>

pkgname=quantlib
_pkgname=QuantLib
pkgver=1.6
pkgrel=1
pkgdesc="A free/open-source library for quantitative finance."
arch=('i686' 'x86_64')
url="http://quantlib.org"
license=('BSD')
options=(!libtool)
depends=('boost-libs' 'sh')
makedepends=('make' 'boost' 'gcc')
source=(https://github.com/lballabio/$pkgname/archive/$_pkgname-v$pkgver.tar.gz)
md5sums=('e5ed785718e2e6352d32a304b521a206')

build() {
  cd "$srcdir/$pkgname-$_pkgname-v$pkgver/$_pkgname"
  ./autogen.sh
  ./configure --prefix=/usr
  make 
}

package() {
  cd "$srcdir/$pkgname-$_pkgname-v$pkgver/$_pkgname"
  make DESTDIR="$pkgdir/" install
  install -D -m644 LICENSE.TXT $pkgdir/usr/share/licenses/$pkgname/LICENSE.TXT
}

# vim:set ts=2 sw=2 et:
