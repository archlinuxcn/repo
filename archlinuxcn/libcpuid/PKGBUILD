# Maintainer: X0rg

pkgname=libcpuid
pkgver=0.5.1
pkgrel=1
pkgdesc="A small C library for x86 CPU detection and feature extraction"
arch=('i686' 'x86_64')
url="http://libcpuid.sourceforge.net"
license=('BSD')
depends=('glibc')
makedepends=('git' 'cmake' 'ninja' 'doxygen')
source=("$pkgname-$pkgver.tar.gz::https://github.com/anrieff/libcpuid/archive/v$pkgver.tar.gz")
sha512sums=('d725bc82e5aa2db69cea7b3590afbe11d6028cf4802fde8d498b4f1cc6d823e73d71b89a453d81bf996d97b36a71f6c00d0f6e8292b72f2be8a64b5d59c01861')

build() {
	cmake -S "$srcdir/$pkgname-$pkgver" -B build -GNinja -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_INSTALL_PREFIX=/usr
	cmake --build build
}

package() {
	DESTDIR="$pkgdir" cmake --install build
	install -Dvm644 "$srcdir/$pkgname-$pkgver/COPYING" "$pkgdir/usr/share/licenses/$pkgname/COPYING"
}
