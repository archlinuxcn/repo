# $Id: PKGBUILD 106884 2014-03-09 12:49:50Z bpiotrowski $
# Upstream Maintainer: Dave Reisner <dreisner@archlinux.org>
# Contributor: judd <jvinet@zeroflux.org>
# Maintainer: Fantix King <fantix.king at gmail.com>

_pkgbasename=util-linux
pkgname=libx32-$_pkgbasename
pkgver=2.24.1
pkgrel=1
pkgdesc="Miscellaneous system utilities for Linux (x32 ABI)"
url='http://www.kernel.org/pub/linux/utils/util-linux/'
arch=('x86_64')
depends=('libx32-glibc' "$_pkgbasename")
makedepends=('gcc-multilib-x32')
provides=('libx32-util-linux-ng')
conflicts=('libx32-util-linux-ng')
replaces=('libx32-util-linux-ng')
license=('GPL2')
options=('!libtool' '!emptydirs')
source=("ftp://ftp.kernel.org/pub/linux/utils/util-linux/v2.24/util-linux-$pkgver.tar.xz")
md5sums=('88d46ae23ca599ac5af9cf96b531590f')

build() {
  cd "$_pkgbasename-$pkgver"

  ./configure \
      CC="${CC:-cc} -mx32" \
      PKG_CONFIG_PATH="/usr/libx32/pkgconfig" \
      --without-ncurses \
      --libdir=/usr/libx32

  make lib{uuid,blkid,mount}.la
}

package() {
  make -C "$_pkgbasename-$pkgver" \
    DESTDIR="$pkgdir" \
    install-usrlib_execLTLIBRARIES \
    install-pkgconfigDATA
}
