# $Id: PKGBUILD 127534 2015-02-10 20:30:52Z bluewind $
# Maintainer: judd <jvinet@zeroflux.org>
# x32 Maintainer: Fantix King <fantix.king at gmail.com>

_pkgbasename=libgpg-error
pkgname=libx32-$_pkgbasename
pkgver=1.18
pkgrel=1.1
pkgdesc="Support library for libgcrypt (x32 ABI)"
arch=(x86_64)
url="http://www.gnupg.org"
license=('LGPL')
depends=('libx32-glibc' $_pkgbasename)
makedepends=(gcc-multilib-x32)
options=(!libtool)
source=(ftp://ftp.gnupg.org/gcrypt/libgpg-error/${_pkgbasename}-${pkgver}.tar.bz2)
  #ftp://ftp.franken.de/pub/crypt/mirror/ftp.gnupg.org/gcrypt/libgpg-error/${pkgname}-${pkgver}.tar.bz2)
sha1sums=('7ba54f939da023af8f5b3e7a421a32eb742909c4')

build() {
  export CC="gcc -mx32"
  export CXX="g++ -mx32"
  export PKG_CONFIG_PATH="/usr/libx32/pkgconfig"

  cd "${srcdir}"/${_pkgbasename}-${pkgver}
  ./configure --prefix=/usr --libdir=/usr/libx32
  make
}

check() {
  cd "${srcdir}"/${_pkgbasename}-${pkgver}
  make check
}

package() {
  cd "${srcdir}"/${_pkgbasename}-${pkgver}
  make DESTDIR="${pkgdir}/" install

  rm -rf "${pkgdir}"/usr/{include,share,bin}
}
