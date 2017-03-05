# Maintainer: Stephen Zhang <zsrkmyn at gmail dot com>

pkgdesc='Lua interface to QT library'
pkgname='torch7-qtlua-git'
pkgver=r81.a29e8a7
pkgrel=1
makedepends=('cmake' 'git')
depends=('torch7-git>=r819' 'qt5-base')
conflicts=('torch7-qtlua')
provides=('torch7-qtlua')
arch=('x86_64' 'i686')
url='https://github.com/torch/qtlua'
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
	[ ! -d build ] && mkdir build
	cd build
	cmake .. \
		-DCMAKE_INSTALL_PREFIX=/usr \
		-DCMAKE_BUILD_TYPE=Release \
		-DLUA_INCDIR=/usr/include/lua5.1 \
		-DLUA_LIBDIR=/usr/lib/lua/5.1 \
		-DLUA=luajit \
		-DLUA_BINDIR=/usr/bin \
		-DLUADIR=/usr/share/lua/5.1/ \
		-DLIBDIR=/usr/lib/lua/5.1 \
		-DCONFDIR=/usr/share/
	make
}

package () {
	cd "${pkgname}/build"
	make DESTDIR="${pkgdir}" install
}
