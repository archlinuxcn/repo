#$Id: PKGBUILD 104722 2014-01-24 21:04:10Z bluewind $
# Maintainer: Florian Pritz <bluewind@xinu.at>
# Contributor: Hugo Doria <hugo@archlinux.org>
# x32 Maintainer: Fantix King <fantix.king at gmail.com>

_pkgbasename=libcap
pkgname=libx32-$_pkgbasename
pkgver=2.24
pkgrel=1.1
pkgdesc="POSIX 1003.1e capabilities (x32 ABI)"
arch=(x86_64)
url="http://www.kernel.org/pub/linux/libs/security/linux-privs/"
license=('GPL2')
depends=('libx32-attr' $_pkgbasename)
makedepends=('gcc-multilib-x32')
source=(https://www.kernel.org/pub/linux/libs/security/linux-privs/libcap2/libcap-${pkgver}.tar.xz)
md5sums=('d43ab9f680435a7fff35b4ace8d45b80')

build() {
  cd "${srcdir}/${_pkgbasename}-${pkgver}"

  export PKG_CONFIG_PATH="/usr/libx32/pkgconfig"

  make -C libcap CC="gcc -mx32" prefix=/usr lib=libx32
}

package() {
  cd "${srcdir}/${_pkgbasename}-${pkgver}"

  make -C libcap prefix=/usr lib=libx32 DESTDIR=${pkgdir} install
  chmod 755 ${pkgdir}/usr/libx32/libcap.so.${pkgver}

  rm -rf "${pkgdir}/usr/include"
}
