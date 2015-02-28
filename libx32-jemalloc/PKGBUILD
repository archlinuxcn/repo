# $Id: PKGBUILD 224120 2014-10-08 19:52:45Z bpiotrowski $
# Maintainer: Massimiliano Torromeo <massimiliano.torromeo@gmail.com>
# Contributor: Kovivchak Evgen <oneonfire@gmail.com>
# x32 Maintainer: Fantix King <fantix.king@gmail.com>

_pkgbasename=jemalloc
pkgname=libx32-jemalloc
pkgver=3.6.0
pkgrel=1.1
pkgdesc="General-purpose scalable concurrent malloc implementation (x32 ABI)"
arch=('x86_64')
license=('BSD')
url="http://www.canonware.com/jemalloc/"
depends=('libx32-glibc')
makedepends=('autoconf' 'make' 'bash')
optdepends=(
	'perl: memory profiler'
)
source=(http://www.canonware.com/download/jemalloc/$_pkgbasename-$pkgver.tar.bz2
        jemalloc-stub.h)

build() {
	cd "$srcdir/$_pkgbasename-$pkgver"

	export CC="gcc -mx32"
	export CXX="g++ -mx32"
	export PKG_CONFIG_PATH="/usr/libx32/pkgconfig"

	CFLAGS="$CFLAGS -std=gnu11" ./configure --prefix=/usr --libdir=/usr/libx32
	make
}

package() {
	install="${pkgname}.install"

	cd "$srcdir/$_pkgbasename-$pkgver"
	make DESTDIR="$pkgdir" install
	rm "$pkgdir"/usr/bin/pprof
	mv "$pkgdir"/usr/bin/jemalloc{,-x32}.sh
	mv "$pkgdir"/usr/include/jemalloc/jemalloc{,-x32}.h
	install -Dm644 "${srcdir}/jemalloc-stub.h" "${pkgdir}/usr/include/jemalloc/jemalloc-stub.h"
	chmod 644 "$pkgdir"/usr/libx32/*.a

	rm -r "$pkgdir/usr/share"
	mkdir -p "$pkgdir/usr/share/licenses"
	ln -s $_pkgbasename "$pkgdir/usr/share/licenses/$pkgname"
}

sha256sums=('e16c2159dd3c81ca2dc3b5c9ef0d43e1f2f45b04548f42db12e7c12d7bdf84fe'
            '58f8b77e15df58934d9138d298fd4005d37b78ace48de757af2fea8deaf347ff')
