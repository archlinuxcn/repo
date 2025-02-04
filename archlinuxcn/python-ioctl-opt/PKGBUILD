# Maintainer: Martin Rys <https://rys.rs/contact> | Toss a coin on https://rys.rs/donate

pkgname=python-ioctl-opt
_reponame=ioctl-opt
pkgver=1.3
pkgrel=2
pkgdesc="Pythonified Linux asm-generic/ioctl.h"
url="https://pypi.org/project/ioctl-opt/"
arch=(any)
license=('GPL-2.0-only')
depends=(
	'python'
)
makedepends=(
	'git'
	'python-build'
	'python-installer'
	'python-setuptools'
)
source=("https://pypi.org/packages/source/${_reponame::1}/${_reponame}/${_reponame}-${pkgver}.tar.gz")
sha256sums=('5ed4f9a80d2e02e152a43d3648d7ed8821a0aac5ea88ecc5fcc14460ff7cf2f9')

build() {
	cd "${srcdir}/${_reponame}-${pkgver}"
	python -m build --wheel --no-isolation
}

package() {
	cd "${srcdir}/${_reponame}-${pkgver}"

	python -m installer --destdir="${pkgdir}" dist/*.whl

	install -d "${pkgdir}/usr/share/licenses/${pkgname}/"
	cp ./COPYING "${pkgdir}/usr/share/licenses/${pkgname}/"
}
