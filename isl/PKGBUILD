#  Maintainer: Kritias     <theodoridisgr@gmail.com>
# Contributor: sudokode    <sudokode@gmail.com>
# Contributor: Allan McRae <allan@archlinux.org>

pkgname=isl
pkgver=0.20
pkgrel=4
pkgdesc="Library for manipulating sets and relations of integer points bounded by linear constraints"
arch=('i686' 'x86_64')
url="http://isl.gforge.inria.fr/"
makedepends=('git')
depends=('gmp')
license=('MIT')
conflicts=('isl-git' 'isl14' 'isl15' 'isl16' 'isl17')
source=("isl::git+http://repo.or.cz/isl.git#tag=isl-${pkgver}")
sha256sums=('SKIP')

build() {
  cd ${srcdir}/${pkgname}
  ./autogen.sh
  ./configure --prefix=/usr
  make
}

check() {
  cd ${srcdir}/${pkgname}
  make check
}

package() {
  cd ${srcdir}/${pkgname}

  make DESTDIR="$pkgdir" install

  install -dm755 "$pkgdir"/usr/share/gdb/auto-load/usr/lib/
  mv "$pkgdir"/usr/lib/libisl.so.*-gdb.py "$pkgdir"/usr/share/gdb/auto-load/usr/lib/
  
  install -Dm644 LICENSE "$pkgdir"/usr/share/licenses/isl/LICENSE
}
