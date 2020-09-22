# Maintainer: Otreblan <otreblain@gmail.com>

pkgname=libinih
pkgver=51
pkgrel=2
epoch=
pkgdesc="Simple .INI file parser in C, good for embedded systems"
arch=('x86_64')
url="https://github.com/benhoyt/inih"
license=('BSD')
groups=()
depends=('gcc-libs')
makedepends=('meson')
checkdepends=()
optdepends=()
provides=("$pkgname.so=0-64" "libINIReader.so=0-64")
conflicts=()
source=("$pkgname-$pkgver.tar.gz::$url/archive/r$pkgver.tar.gz")
sha256sums=("132361da6d3172760a40319722b50244aee1b7ce7077a0dd8805881e6a8ea4aa")

build() {
	arch-meson "${pkgname#lib}-r$pkgver" build \
		-Ddefault_library=shared \
		-Ddistro_install=true \
		-Dwith_INIReader=true

	meson compile -C build
}

package() {
	DESTDIR="$pkgdir" meson install -C build

	cd "$srcdir/${pkgname#lib}-r$pkgver"
	install -Dm644 LICENSE.txt -t "$pkgdir/usr/share/licenses/$pkgname"
}
