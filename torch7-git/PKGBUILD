# Maintainer: Adrián Pérez de Castro <aperez@igalia.com>
pkgdesc='LuaJIT-based scientific computing framework'
pkgname='torch7-git'
pkgver=r1049.65255ba
pkgrel=1
url='http://torch.ch'
source=("${pkgname}::git://github.com/torch/torch7")
depends=('luajit' 'blas' 'lapack' 'torch7-cwrap-git' 'torch7-paths-git')
optdepends=('torch7-trepl-git: Interactive REPL shell')
conflicts=('torch7')
provides=('torch7')
makedepends=('cmake' 'git')
arch=('x86_64' 'i686')
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
		-DCMAKE_BUILD_TYPE=Release \
		-DCMAKE_INSTALL_PREFIX=/usr \
		-DLUADIR=/usr/share/lua/5.1 \
		-DLIBDIR=/usr/lib/lua/5.1 \
		-DLUA_BINDIR=/usr/bin \
		-DLUA_INCDIR=/usr/include/luajit-2.0 \
		-DLUA_LIBDIR=/usr/lib \
		-DLUALIB=/usr/lib/libluajit-5.1.so \
		-DLUA=/usr/bin/luajit
	make
}

package () {
	cd "${pkgname}"
	make DESTDIR="${pkgdir}" install
}

