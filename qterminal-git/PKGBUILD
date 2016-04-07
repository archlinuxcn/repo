# Maintainer: Jerome Leclanche <jerome@leclan.ch>

_pkgname=qterminal
pkgname=$_pkgname-git
pkgver=0.6.0.98.g7f83f86
pkgrel=1
pkgdesc="Lightweight Qt-based terminal emulator"
arch=("i686" "x86_64")
url="https://github.com/lxde/qterminal"
license=("GPL2")
provides=("$_pkgname")
conflicts=("$_pkgname")
depends=("qtermwidget")
makedepends=("git" "cmake" "qt5-tools")
source=("git+https://github.com/lxde/$_pkgname.git")
sha256sums=("SKIP")


pkgver() {
	cd "$srcdir/$_pkgname"
	git describe --always | sed "s/-/./g"
}

build() {
	mkdir -p build
	cd build
	cmake "$srcdir/$_pkgname" \
		-DCMAKE_INSTALL_PREFIX=/usr \
		-DCMAKE_INSTALL_LIBDIR=lib
	make
}

package() {
	cd build
	make DESTDIR="$pkgdir" install
}
