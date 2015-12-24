# $Id: PKGBUILD 148405 2015-12-04 23:06:44Z dreisner $
# Maintainer: Dave Reisner <dreisner@archlinux.org>
# Contributor: judd <jvinet@zeroflux.org>
# x32 Maintainer: Fantix King <fantix.king at gmail.com>

_pkgbasename=util-linux
pkgname=libx32-$_pkgbasename
pkgver=2.27.1
_pkgver=(${pkgver//./ })
_pkgver=${_pkgver[0]}.${_pkgver[1]}
pkgrel=1.1
pkgdesc="Miscellaneous system utilities for Linux (x32 ABI)"
url='http://www.kernel.org/pub/linux/utils/util-linux/'
arch=('x86_64')
depends=('libx32-glibc' "$_pkgbasename")
provides=('libuuid.so' 'libblkid.so' 'libfdisk.so' 'libmount.so' 'libsmartcols.so')
makedepends=('gcc-multilib-x32')
license=('GPL2')
options=('!libtool' '!emptydirs')
source=("ftp://ftp.kernel.org/pub/linux/utils/util-linux/v${_pkgver}/util-linux-$pkgver.tar.xz")
md5sums=('3cd2698d1363a2c64091c2dadc974647')

build() {
  cd "$_pkgbasename-$pkgver"

  ./configure \
      CC="${CC:-cc} -mx32" \
      PKG_CONFIG_PATH="/usr/libx32/pkgconfig" \
      --libdir=/usr/libx32

  make lib{uuid,blkid,fdisk,mount,smartcols}.la
}

package() {
  make -C "$_pkgbasename-$pkgver" \
    DESTDIR="$pkgdir" \
    install-usrlib_execLTLIBRARIES \
    install-pkgconfigDATA
}
