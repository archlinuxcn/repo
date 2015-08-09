# Maintainer: Jerome Leclanche <jerome@leclan.ch>

_pkgname=libqtxdg
pkgname=$_pkgname-git
pkgver=1.2.0.13.gab0f65c
pkgrel=1
pkgdesc="Library providing freedesktop.org specs implementations for Qt."
arch=("i686" "x86_64")
url="http://lxqt.org"
license=("GPL2")
depends=("qt5-base")
makedepends=("git" "cmake" "qt5-tools")
provides=("$_pkgname")
conflicts=("$_pkgname-qt5-git" "$_pkgname")
replaces=("$_pkgname-qt5-git")
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
