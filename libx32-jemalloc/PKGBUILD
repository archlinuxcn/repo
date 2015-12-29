# $Id: PKGBUILD 249759 2015-10-25 19:33:24Z bpiotrowski $
# Maintainer:  Bartłomiej Piotrowski <bpiotrowski@archlinux.org>
# Contributor: Massimiliano Torromeo <massimiliano.torromeo@gmail.com>
# Contributor: Kovivchak Evgen <oneonfire@gmail.com>
# x32 Maintainer: Fantix King <fantix.king@gmail.com>

_pkgbasename=jemalloc
pkgname=libx32-jemalloc
pkgver=4.0.4
pkgrel=1.1
pkgdesc='General-purpose scalable concurrent malloc implementation (x32 ABI)'
arch=('x86_64')
license=('BSD')
url='http://www.canonware.com/jemalloc/'
depends=('libx32-glibc' "${_pkgbasename}")
provides=('libjemalloc.so')
optdepends=('perl: for jeprof')
source=(http://www.canonware.com/download/jemalloc/$_pkgbasename-$pkgver.tar.bz2
        jemalloc-stub.h)
md5sums=('687c5cc53b9a7ab711ccd680351ff988'
         '2d00976616cb0159bc81108bcb028fbe')

build() {
  cd $_pkgbasename-$pkgver

  export CC="gcc -mx32"
  export CXX="g++ -mx32"
  export PKG_CONFIG_PATH="/usr/libx32/pkgconfig"

  ./configure --prefix=/usr --libdir=/usr/libx32
  make
}

package() {
  install="${pkgname}.install"

  cd $_pkgbasename-$pkgver
  make DESTDIR="$pkgdir" install
  find "$pkgdir" -name \*.a -type f -exec chmod 644 '{}' \;
  mv "$pkgdir"/usr/bin/jeprof{,-x32}
  mv "$pkgdir"/usr/bin/jemalloc-config{,-x32}
  mv "$pkgdir"/usr/bin/jemalloc{,-x32}.sh
  mv "$pkgdir"/usr/include/jemalloc/jemalloc{,-x32}.h
  install -Dm644 "${srcdir}/jemalloc-stub.h" "${pkgdir}/usr/include/jemalloc/jemalloc-stub.h"

  rm -r "$pkgdir/usr/share"
  mkdir -p "$pkgdir/usr/share/licenses"
  ln -s $_pkgbasename "$pkgdir/usr/share/licenses/$pkgname"
}
