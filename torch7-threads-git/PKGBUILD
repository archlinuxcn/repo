# Maintainer: Adrián Pérez de Castro <aperez@igalia.com>
pkgname='torch7-threads-git'
pkgdesc='Threads for Lua and LuaJIT. Transparent exchange of data between threads is allowed thanks to torch serialization.'
pkgver=r90.9e31123
pkgrel=1
makedepends=('cmake' 'git')
depends=('torch7-git>=r819')
conflicts=('torch7-threads')
provides=('torch7-threads')
arch=('x86_64' 'i686')
url='https://github.com/torch/threads'
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
	mv "${pkgdir}/usr/lib/libthreads.so" "${pkgdir}/usr/lib/lua/5.1/"
#	mv "${pkgdir}/usr/lib/libthreadsmain.so" "${pkgdir}/usr/lib/lua/5.1/"

	# Move pure Lua modules
	mkdir -p "${pkgdir}/usr/share/lua/5.1"
	mv "${pkgdir}/usr/lua/threads" "${pkgdir}/usr/share/lua/5.1/"
	rm -rf "${pkgdir}/usr/lua"
}
