# Maintainer: Moritz Lipp <mlq@pwmt.org>

pkgname=bear
_pkgname=Bear
pkgver=2.3.9
pkgrel=1
pkgdesc="tool to generate compilation database for clang tooling"
arch=('i686' 'x86_64')
url="https://github.com/rizsotto/Bear"
license=('GPL3')
makedepends=('cmake' 'make')
depends=('python>=2.7')
conflicts=('bear')
provides=('bear')
source=(https://github.com/rizsotto/$_pkgname/archive/$pkgver.tar.gz)
md5sums=('e0ec02a038b8602a5c4cfa4b00111ce5')

build() {
	cd "$srcdir/$_pkgname-$pkgver"
  cmake \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_INSTALL_SYSCONFDIR=/etc \
    .
	make all
}

check() {
	cd "$srcdir/$_pkgname-$pkgver"
  PATH=/usr/bin:$PATH make -k check
}

package() {
	cd "$srcdir/$_pkgname-$pkgver"
	make DESTDIR="$pkgdir/" install

  if [ $CARCH = "x86_64" ]; then
    mv $pkgdir/usr/lib64 $pkgdir/usr/lib
  fi
}
