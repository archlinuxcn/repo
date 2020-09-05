# Maintainer: X0rg

pkgname=libcpuid
pkgver=0.5.0
pkgrel=1
pkgdesc="A small C library for x86 CPU detection and feature extraction"
arch=('i686' 'x86_64')
url="http://libcpuid.sourceforge.net"
license=('BSD')
depends=('glibc')
makedepends=('git' 'cmake' 'ninja' 'doxygen')
source=("$pkgname-$pkgver.tar.gz::https://github.com/anrieff/libcpuid/archive/v$pkgver.tar.gz")
sha512sums=('c98f4a95e111da5a4ac54d6f6e25c882f01e6984fcf2f8c1d1c8437cac54ea057233aab05a19c4a1ffa800d54aebf089ca8be6b26b89ff625df382a2984ee462')

build() {
	cmake -S "$srcdir/$pkgname-$pkgver" -B build -GNinja -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_INSTALL_PREFIX=/usr
	cmake --build build
}

package() {
	DESTDIR="$pkgdir" cmake --install build
	install -Dvm644 "$srcdir/$pkgname-$pkgver/COPYING" "$pkgdir/usr/share/licenses/$pkgname/COPYING"
}
