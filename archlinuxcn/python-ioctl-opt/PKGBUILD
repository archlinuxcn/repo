# Maintainer: Martin Rys <https://rys.rs/contact> | Toss a coin on https://rys.rs/donate

pkgname=python-ioctl-opt
pkgver=1.3
pkgrel=3
pkgdesc="Pythonified Linux asm-generic/ioctl.h"
url="https://github.com/vpelletier/python-ioctl-opt"
arch=(any)
license=('GPL-2.0-or-later')
depends=(
	'python'
)
makedepends=(
	'git'
	'python-build'
	'python-installer'
	'python-setuptools'
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/vpelletier/python-ioctl-opt/archive/${pkgver}.tar.gz")
sha256sums=('78af049a170f4194a0ea3804ea5f37b55c8faccdb9c870f82c3ca550ba98b44f')

build() {
	cd "${srcdir}/${pkgname}-${pkgver}"
	python -m build --wheel --no-isolation
}

package() {
	cd "${srcdir}/${pkgname}-${pkgver}"

	python -m installer --destdir="${pkgdir}" dist/*.whl

	install -Dm644 COPYING "${pkgdir}/usr/share/licenses/${pkgname}/COPYING"
}
