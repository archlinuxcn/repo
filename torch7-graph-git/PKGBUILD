# Maintainer: Jingbei Li <i@jingbei.lli>
pkgname='torch7-graph-git'
pkgdesc='Graph Computation'
pkgver=r70.47afe90
pkgrel=1
makedepends=('cmake' 'git')
depends=('torch7-git>=r819')
arch=('x86_64' 'i686')
url='https://github.com/torch/graph'
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

	# Move pure Lua modules
	mkdir -p "${pkgdir}/usr/share/lua/5.1"
	mv "${pkgdir}/usr/lua/graph" "${pkgdir}/usr/share/lua/5.1/"
	rm -rf "${pkgdir}/usr/lua"
}

