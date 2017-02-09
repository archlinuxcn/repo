# Maintainer: Jingbei Li <i@jingbei.li>
pkgdesc='A numeric optimization package for Torch.'
pkgname='torch7-optim-git'
pkgver=1.0.3.0.r175.g5e11b9f
pkgrel=1
makedepends=('cmake' 'git')
depends=('torch7-git>=r819')
conflicts=('torch7-optim')
provides=('torch7-optim')
arch=('x86_64' 'i686')
url='https://github.com/torch/optim'
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
	mv "${pkgdir}/usr/lua/optim" "${pkgdir}/usr/share/lua/5.1/"
	rm -rf "${pkgdir}/usr/lua"
}
