# $Id: PKGBUILD 89550 2013-04-29 23:08:08Z lcarlier $
# Upstream Maintainer: Ionut Biru <ibiru@archlinux.org>
# Contributor: Pierre Schmitz <pierre@archlinux.de>
# Maintainer: Fantix King <fantix.king at gmail.com>

_pkgbasename=zlib
pkgname=libx32-$_pkgbasename
pkgver=1.2.8
pkgrel=1
pkgdesc='Compression library implementing the deflate compression method found in gzip and PKZIP (x32 ABI)'
arch=('x86_64')
license=('custom')
url="http://www.zlib.net/"
depends=('libx32-glibc' "$_pkgbasename")
makedepends=('gcc-multilib-x32')
source=("http://zlib.net/current/zlib-${pkgver}.tar.gz")
md5sums=('44d667c142d7cda120332623eab69f40')

build() {
	export CC="gcc -mx32"
	export CXX="g++ -mx32"
	export PKG_CONFIG_PATH="/usr/libx32/pkgconfig"

	cd ${srcdir}/zlib-$pkgver
	./configure --prefix=/usr \
		--libdir=/usr/libx32
	make
}

check() {
	cd ${srcdir}/zlib-$pkgver
	make test
}

package() {
	cd ${srcdir}/zlib-$pkgver
	make install DESTDIR=${pkgdir}

	rm -rf "${pkgdir}"/usr/{include,share,bin}
	mkdir -p "$pkgdir/usr/share/licenses"
	ln -s $_pkgbasename "$pkgdir/usr/share/licenses/$pkgname"
}
