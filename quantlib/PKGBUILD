# Maintainer: Allen Hoffmeyer <allen dot hoffmeyer at gmail dot com>
#               (adapted from work by Louis R. Marascio <lrm at fitnr dot com>)
# Contributor: trader <trader9 at gawab dot com>
# Contributor: masutu <masutu dot arch at googlemail dot com>

pkgname=quantlib
_pkgname=QuantLib
pkgver=1.9
pkgrel=1
pkgdesc="A free/open-source library for quantitative finance."
arch=('i686' 'x86_64')
url="http://quantlib.org"
license=('BSD')
options=(!libtool)
depends=('boost-libs' 'sh')
makedepends=('make' 'boost' 'gcc')
source=(http://downloads.sourceforge.net/project/$pkgname/$_pkgname/$pkgver/$_pkgname-$pkgver.tar.gz)
md5sums=('901944bc4f2daa25c57845300b772110')

build() {
  cd "$srcdir"/"$_pkgname-$pkgver"/
  ./autogen.sh
  ./configure --prefix=/usr
  make -j`nproc`
}

package() {
  cd "$srcdir"/"$_pkgname-$pkgver"/
  make DESTDIR="$pkgdir/" install
  install -D -m644 LICENSE.TXT "$pkgdir/usr/share/licenses/$pkgname/LICENSE.TXT"
}

# vim:set ts=2 sw=2 et:
