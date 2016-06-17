# Maintainer: Jerome Leclanche <jerome@leclan.ch>

_pkgname=pcmanfm-qt
pkgname=$_pkgname-git
pkgver=0.10.1.40.gc23f78e
pkgrel=1
pkgdesc="The LXQt file manager, Qt port of PCManFM"
arch=("i686" "x86_64")
url="http://lxqt.org"
license=("GPL2")
depends=("liblxqt-git" "libfm-qt-git" "lxmenu-data" "qt5-x11extras")
makedepends=("git" "cmake" "qt5-tools")
provides=("$_pkgname")
conflicts=("$_pkgname")
install="$_pkgname.install"
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
