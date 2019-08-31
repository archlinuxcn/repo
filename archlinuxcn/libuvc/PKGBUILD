# Maintainer: Maarten de Vries <maarten@de-vri.es>
# Based on AUR3 PKGBUILD by Ken Tossell <ken@tossell.net>

pkgname=libuvc
pkgver=0.0.6
pkgrel=1
pkgdesc="a cross-platform library for USB video devices"
arch=('i686' 'x86_64')
url="https://int80k.com/libuvc/"
license=('BSD')
depends=('libusb' 'libjpeg')
makedepends=('cmake')
source=("$pkgname-$pkgver.tar.gz::https://github.com/ktossell/libuvc/archive/v$pkgver.tar.gz")
sha256sums=('42175a53c1c704365fdc782b44233925e40c9344fbb7f942181c1090f06e2873')

prepare() {
	rm -rf "$srcdir/build"
	mkdir -p "$srcdir/build"
	cd "$srcdir/build"

	cmake "$srcdir/libuvc-$pkgver" \
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
