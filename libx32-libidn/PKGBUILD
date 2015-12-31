# $Id: PKGBUILD 138465 2015-08-18 03:12:35Z fyan $
# Maintainer: Florian Pritz <bluewind@xinu.at>
# x32 Maintainer: Fantix King <fantix.king at gmail.com> 
_pkgbasename=libidn
pkgname=libx32-$_pkgbasename
pkgver=1.32
pkgrel=1.1
pkgdesc="Implementation of the Stringprep, Punycode and IDNA specifications (x32 ABI)"
url="http://www.gnu.org/software/libidn/"
arch=('x86_64')
license=('GPL3' 'LGPL')
depends=('libx32-glibc' "$_pkgbasename>=$pkgver")
makedepends=('gcc-multilib-x32')
options=('!libtool')
source=(http://ftp.gnu.org/gnu/${_pkgbasename}/${_pkgbasename}-${pkgver}.tar.gz)
sha1sums=('ddd018611b98af7c67d434aa42d15d39f45129f5')

build() {
  cd ${srcdir}/${_pkgbasename}-${pkgver}
  ./configure --prefix=/usr --libdir=/usr/libx32 CC='gcc -mx32'
  make
}

package() {
  cd ${srcdir}/${_pkgbasename}-${pkgver}
  make DESTDIR=${pkgdir} install
  rm -rf ${pkgdir}/usr/{bin,include,share}
}
