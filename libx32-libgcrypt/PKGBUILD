# $Id: PKGBUILD 117893 2014-08-26 08:57:32Z bluewind $
# Maintainer: Andreas Radke <andyrtr@archlinux.org>
# x32 Maintainer: Fantix King <fantix.king at gmail.com>

_pkgbasename=libgcrypt
pkgname=libx32-$_pkgbasename
pkgver=1.6.2
pkgrel=1.1
pkgdesc="General purpose cryptographic library based on the code from GnuPG (x32 ABI)"
arch=(x86_64)
url="http://www.gnupg.org"
license=('LGPL')
depends=('libx32-libgpg-error>=1.10-2' $_pkgbasename)
makedepends=(gcc-multilib-x32 libtool-multilib)
source=(ftp://ftp.gnupg.org/gcrypt/${_pkgbasename}/${_pkgbasename}-${pkgver}.tar.bz2
  libgcrypt-1.4.5-x32.patch
)
sha1sums=('cc31aca87e4a3769cb86884a3f5982b2cc8eb7ec'
          '0d23f2f17b9f4f6461abb4f8f5115f9db3143841')

build() {
  export CC="gcc -mx32"
  export CXX="g++ -mx32"
  export PKG_CONFIG_PATH="/usr/libx32/pkgconfig"

  cd ${_pkgbasename}-${pkgver}

  patch -p1 -i ${srcdir}/libgcrypt-1.4.5-x32.patch

  ./configure --prefix=/usr --disable-static --disable-padlock-support \
              --libdir=/usr/libx32 --enable-shared
  make
}

package() {
  cd ${_pkgbasename}-${pkgver}

  make DESTDIR=${pkgdir} install
  rm -rf "${pkgdir}"/usr/{include,share,bin,sbin}
}
