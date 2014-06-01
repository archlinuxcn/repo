# $Id: PKGBUILD 108638 2014-03-30 21:45:14Z bluewind $
# Upstream Maintainer: Tobias Powalowski <tpowa@archlinux.org>
# Maintainer: Fantix King <fantix.king at gmail.com>
_pkgbasename=keyutils
pkgname=libx32-$_pkgbasename
pkgver=1.5.9
pkgrel=1
pkgdesc="Linux Key Management Utilities (x32 ABI)"
arch=(x86_64)
url="http://www.kernel.org"
license=('GPL2' 'LGPL2.1')
depends=(libx32-glibc $_pkgbasename)
makedepends=(gcc-multilib-x32)
source=(http://people.redhat.com/~dhowells/$_pkgbasename/$_pkgbasename-$pkgver.tar.bz2)
md5sums=('7f8ac985c45086b5fbcd12cecd23cf07')

build() {
  cd "$srcdir/$_pkgbasename-$pkgver"
  
  export CC="gcc -mx32"
  export CXX="g++ -mx32"
  export PKG_CONFIG_PATH="/usr/libx32/pkgconfig"

  sed -i -e 's/^\(USR\)\?LIBDIR\s*:=.*$/\1LIBDIR=\/usr\/libx32/' Makefile
  make CFLAGS="${CFLAGS}" LDFLAGS="${LDFLAGS}"
}

package() {
  cd "$srcdir/$_pkgbasename-$pkgver"
  make DESTDIR="$pkgdir" install

  rm -rf "${pkgdir}"/{usr/{include,share,bin,sbin},etc,{s,}bin}
}
