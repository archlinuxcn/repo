# Maintainer : Andrew Sun  <adsun701 at gmail dot com>
# Contributor: Kritias     <theodoridisgr at gmail dot com>
# Contributor: sudokode    <sudokode at gmail dot com>
# Contributor: Allan McRae <allan at archlinux dot org>

pkgname=isl
pkgver=0.24
pkgrel=1
pkgdesc="Library for manipulating sets and relations of integer points bounded by linear constraints"
arch=('i686' 'x86_64')
url="http://isl.gforge.inria.fr/"
depends=('gmp')
license=('MIT')
conflicts=('isl-git' 'isl14' 'isl15' 'isl16' 'isl17')
source=("http://isl.gforge.inria.fr/isl-${pkgver}.tar.gz")
sha256sums=('26e6e4d60ad59b3fff9948eb36743f0c874e124e410ef5bab930d0f546bc580d')

build() {
  cd ${srcdir}/${pkgname}-${pkgver}
  ./configure --prefix=/usr
  make
}

check() {
  cd ${srcdir}/${pkgname}-${pkgver}
  make check || true
}

package() {
  cd ${srcdir}/${pkgname}-${pkgver}

  make DESTDIR="$pkgdir" install

  install -dm755 "$pkgdir"/usr/share/gdb/auto-load/usr/lib/
  mv "$pkgdir"/usr/lib/libisl.so.*-gdb.py "$pkgdir"/usr/share/gdb/auto-load/usr/lib/
  
  install -Dm644 LICENSE "$pkgdir"/usr/share/licenses/isl/LICENSE
}
