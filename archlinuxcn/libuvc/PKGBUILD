# Maintainer: Maarten de Vries <maarten@de-vri.es>
# Based on AUR3 PKGBUILD by Ken Tossell <ken@tossell.net>

pkgname=libuvc
pkgver=0.0.7
pkgrel=1
pkgdesc="a cross-platform library for USB video devices"
arch=('i686' 'x86_64' 'aarch64')
url="https://int80k.com/libuvc/"
license=('BSD')
depends=('glibc' 'libusb' 'libjpeg')
makedepends=('cmake')
source=("$pkgname-$pkgver.tar.gz::https://github.com/ktossell/libuvc/archive/v$pkgver.tar.gz")
sha256sums=('7c6ba79723ad5d0ccdfbe6cadcfbd03f9f75b701d7ba96631eb1fd929a86ee72')

prepare() {
	rm -rf "$srcdir/build"
	mkdir -p "$srcdir/build"
	cd "$srcdir/build"

	cmake "$srcdir/libuvc-$pkgver" \
		-DCMAKE_SHARED_LINKER_FLAGS="$LDFLAGS" \
		-DCMAKE_INSTALL_PREFIX=/usr \
		-DCMAKE_INSTALL_LIBDIR=lib
}

build() {
	make -C "$srcdir/build"
}

package() {
	make -C "$srcdir/build" DESTDIR="${pkgdir}" install
	install -m 644 -Dt "$pkgdir/usr/share/licenses/$pkgname" "$srcdir/libuvc-$pkgver/LICENSE.txt"
}
