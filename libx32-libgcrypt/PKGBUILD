# $Id: PKGBUILD 142815 2015-10-02 19:14:21Z bluewind $
# Maintainer: Andreas Radke <andyrtr@archlinux.org>
# x32 Maintainer: Fantix King <fantix.king at gmail.com>

_pkgbasename=libgcrypt
pkgname=libx32-$_pkgbasename
pkgver=1.6.4
pkgrel=1.1
pkgdesc="General purpose cryptographic library based on the code from GnuPG (x32 ABI)"
arch=(x86_64)
url="http://www.gnupg.org"
license=('LGPL')
depends=('libx32-libgpg-error>=1.10-2' $_pkgbasename)
makedepends=(gcc-multilib-x32 libtool-multilib)
source=(ftp://ftp.gnupg.org/gcrypt/${_pkgbasename}/${_pkgbasename}-${pkgver}.tar.bz2{,.sig}
  libgcrypt-1.4.5-x32.patch
)
sha1sums=('ed52add1ce635deeb2f5c6650e52667debd4ec70'
          'SKIP'
          '0d23f2f17b9f4f6461abb4f8f5115f9db3143841')
validpgpkeys=('031EC2536E580D8EA286A9F22071B08A33BD3F06') # "NIIBE Yutaka (GnuPG Release Key) <gniibe@fsij.org>"

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
