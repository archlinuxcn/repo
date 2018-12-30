#  Maintainer: Kritias     <theodoridisgr@gmail.com>
# Contributor: sudokode    <sudokode@gmail.com>
# Contributor: Allan McRae <allan@archlinux.org>

pkgname=isl
pkgver=0.20
pkgrel=5
pkgdesc="Library for manipulating sets and relations of integer points bounded by linear constraints"
arch=('i686' 'x86_64')
url="http://isl.gforge.inria.fr/"
depends=('gmp')
license=('MIT')
conflicts=('isl-git' 'isl14' 'isl15' 'isl16' 'isl17')
source=("http://isl.gforge.inria.fr/isl-${pkgver}.tar.gz")
sha256sums=('cf4ec18538df940ad5d5760af1246825cc58dd295241ab41d3f3962b24f55199')
build() {
  cd ${srcdir}/${pkgname}-${pkgver}
  ./configure --prefix=/usr
  make
}

check() {
  cd ${srcdir}/${pkgname}-${pkgver}
  make check
}

package() {
  cd ${srcdir}/${pkgname}-${pkgver}

  make DESTDIR="$pkgdir" install

  install -dm755 "$pkgdir"/usr/share/gdb/auto-load/usr/lib/
  mv "$pkgdir"/usr/lib/libisl.so.*-gdb.py "$pkgdir"/usr/share/gdb/auto-load/usr/lib/
  
  install -Dm644 LICENSE "$pkgdir"/usr/share/licenses/isl/LICENSE
}
