# Maintainer: Jingbei Li <i@jingbei.lli>
pkgname='torch7-hdf5-git'
pkgdesc='Torch interface to HDF5 library'
pkgver=v0.0.r118.ga4f80cb
pkgrel=2
makedepends=('cmake' 'git' 'hdf5-cpp-fortran')
depends=('torch7-git>=r819' 'hdf5_18-cpp-fortran')
arch=('x86_64' 'i686')
url='https://github.com/deepmind/torch-hdf5'
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
	sed 's/^FILE(WRITE /FILE(WRITE ${DESTDIR}/' -i CMakeLists.txt
	cmake . -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Release -DDESTDIR="${pkgdir}"
	make
}

package () {
	cd "${pkgname}"
	make DESTDIR="${pkgdir}" install

	# Move pure Lua modules
	mkdir -p "${pkgdir}/usr/share/lua/5.1"
	mv "${pkgdir}/usr/lua/hdf5" "${pkgdir}/usr/share/lua/5.1/"
	rm -rf "${pkgdir}/usr/lua"

	# Fix HDF5 libraries
	sed -e 's/""/"\/usr\/include\/hdf5_18"/' -e 's/libhdf5/hdf5_18\/libhdf5/g' -i "${pkgdir}/usr/share/lua/5.1/hdf5/config.lua"
}
