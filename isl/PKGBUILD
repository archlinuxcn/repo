#  Maintainer: Kritias     <theodoridisgr@gmail.com>
# Contributor: sudokode    <sudokode@gmail.com>
# Contributor: Allan McRae <allan@archlinux.org>

pkgname=isl
pkgver=0.20
pkgrel=2
pkgdesc="Library for manipulating sets and relations of integer points bounded by linear constraints"
arch=('i686' 'x86_64')
url="http://isl.gforge.inria.fr/"
depends=('gmp')
license=('MIT')
conflicts=('isl-git' 'isl14' 'isl15' 'isl16' 'isl17')
source=("http://isl.gforge.inria.fr/$pkgname-${pkgver}.tar.xz")
sha256sums=('a5596a9fb8a5b365cb612e4b9628735d6e67e9178fae134a816ae195017e77aa')
build() {
  cd $pkgname-$pkgver

  ./configure --prefix=/usr
  make
}

check() {
  cd $pkgname-$pkgver

  make check
}

package() {
  cd $pkgname-$pkgver

  make DESTDIR="$pkgdir" install

  install -dm755 "$pkgdir"/usr/share/gdb/auto-load/usr/lib/
  mv "$pkgdir"/usr/lib/libisl.so.*-gdb.py "$pkgdir"/usr/share/gdb/auto-load/usr/lib/
  
  install -Dm644 LICENSE "$pkgdir"/usr/share/licenses/isl/LICENSE
}
