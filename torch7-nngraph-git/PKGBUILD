# Maintainer: Jingbei Li <i@jingbei.lli>
pkgname='torch7-nngraph-git'
pkgdesc='Graph Computation for nn'
pkgver=r211.f6aeb88
pkgrel=1
makedepends=('cmake' 'git')
depends=('torch7-git>=r819' 'torch7-nn-git' 'torch7-graph-git')
optdepends=('graphviz:	To display the graphs that you have created.')
arch=('x86_64' 'i686')
url='https://github.com/torch/nngraph'
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
	mv "${pkgdir}/usr/lua/nngraph" "${pkgdir}/usr/share/lua/5.1/"
	rm -rf "${pkgdir}/usr/lua"
}
