# Maintainer: Adrián Pérez de Castro <aperez@igalia.com>
pkgdesc='File name manipulation module for Torch7'
pkgname='torch7-paths-git'
pkgver=r41.68d579a
pkgrel=1
makedepends=('cmake' 'git')
depends=('luajit')
conflicts=('torch7-paths')
provides=('torch7-paths')
arch=('x86_64' 'i686')
url='https://github.com/torch/paths'
license=('BSD')
source=("${pkgname}::git+${url}")
sha512sums=('SKIP')

pkgver () {
	cd "${pkgname}"
	(
		set -o pipefail
		git describe --long 2>/dev/null | sed 's/\([^-]*-g\)/r\1/;s/-/./g' ||
		printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
	)
}

build () {
	cd "${pkgname}"
	cmake . \
		-DCMAKE_INSTALL_PREFIX=/usr \
		-DLUADIR=/usr/share/lua/5.1 \
		-DLIBDIR=/usr/lib/lua/5.1 \
		-DLUALIB=/usr/lib/libluajit-5.1.so \
		-DLUA_INCDIR=/usr/include/luajit-2.0 \
		-DLUA_LIBDIR=/usr/lib
	make
}

package () {
	cd "${pkgname}"
	make DESTDIR="${pkgdir}" install
}
