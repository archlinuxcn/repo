# Maintainer: Adrián Pérez de Castro <aperez@igalia.com>
pkgdesc='A system utility package for Torch.'
pkgname='torch7-sys-git'
pkgver=1.1.0.r12.gcadd701
pkgrel=1
makedepends=('cmake' 'git')
depends=('torch7-git>=r819')
conflicts=('torch7-sys')
provides=('torch7-sys')
arch=('x86_64' 'i686')
url='https://github.com/torch/sys'
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
	cmake . -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Release
	make
}

package () {
	cd "${pkgname}"
	make DESTDIR="${pkgdir}" install

	# Move Lua C module
	mkdir -p "${pkgdir}/usr/lib/lua/5.1"
	mv "${pkgdir}/usr/lib/libsys.so" "${pkgdir}/usr/lib/lua/5.1/"

	# Move pure Lua modules
	mkdir -p "${pkgdir}/usr/share/lua/5.1"
	mv "${pkgdir}/usr/lua/sys" "${pkgdir}/usr/share/lua/5.1/"
	rm -rf "${pkgdir}/usr/lua"
}
