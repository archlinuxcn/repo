# Maintainer: Stephen Zhang <zsrkmyn at gmail dot com>
pkgdesc='Torch C data structures'
pkgname='torch7-tds-git'
pkgver=r78.3f16e88
pkgrel=1
makedepends=('cmake' 'git')
depends=('torch7-git>=r819')
conflicts=('torch7-tds')
provides=('torch7-tds')
arch=('x86_64' 'i686')
url='https://github.com/torch/tds'
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
		-DLUA_CPATH=/usr/lib/lua/5.1 \
		-DLUA_PATH=/usr/share/lua/5.1
	make
}

package () {
	cd "${pkgname}/build"
	make DESTDIR="${pkgdir}" install
}
