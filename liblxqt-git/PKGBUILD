# Maintainer: Jerome Leclanche <jerome@leclan.ch>

_pkgname=liblxqt
pkgname=$_pkgname-git
pkgver=0.10.0.19.g7df67a2
pkgrel=1
pkgdesc="Common base library for LXQt components."
arch=("i686" "x86_64")
url="http://lxqt.org"
license=("GPL2")
depends=("qt5-base" "qt5-x11extras" "kwindowsystem" "libqtxdg")
makedepends=("git" "cmake" "qt5-tools")
provides=("$_pkgname")
conflicts=("$_pkgname")
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
