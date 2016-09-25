# Maintainer: Peter Mattern <pmattern at arcor dot de>
# Contributor: Jerome Leclanche <jerome at leclan dot ch>

_pkgname=libsysstat
pkgname=$_pkgname-git
pkgver=0.3.0.12.g5ef5c4a
pkgrel=1
pkgdesc="Library to query system statistics (net, resource usage, ...)"
arch=("i686" "x86_64" "armv6h")
url="http://lxqt.org"
license=("LGPL2.1")
depends=("qt5-base")
makedepends=("git" "cmake")
provides=("$_pkgname" "$_pkgname-qt5" "$_pkgname-qt5-git")
conflicts=("$_pkgname" "$_pkgname-qt5" "$_pkgname-qt5-git")
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
