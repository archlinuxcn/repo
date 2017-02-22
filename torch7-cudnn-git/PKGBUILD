# Maintainer: Jingbei Li <i@jingbei.li>
pkgdesc='Torch-7 FFI bindings for NVIDIA CuDNN'
pkgname='torch7-cudnn-git'
pkgver=r353.440f0d5
pkgrel=1
makedepends=('cmake' 'git')
depends=('torch7-git>=r819' 'cudnn')
conflicts=('torch7-cudnn')
provides=('torch7-cudnn')
arch=('x86_64' 'i686')
url='https://github.com/soumith/cudnn.torch'
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
	mv "${pkgdir}/usr/lua/cudnn" "${pkgdir}/usr/share/lua/5.1/"
	rm -rf "${pkgdir}/usr/lua"
}
