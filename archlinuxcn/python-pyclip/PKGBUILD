# Maintainer: Imperator Storm <ImperatorStorm11@protonmail.com>
# Contributor: Philip Goto <philip.goto@gmail.com>

_pkgname=pyclip
pkgname=python-${_pkgname}
pkgver=0.7.0
pkgrel=2
pkgdesc='Cross-platform clipboard utilities supporting both binary and text data'
arch=(any)
url="https://pypi.org/project/${_pkgname}/"
license=(Apache)
depends=(python-argparse)
makedepends=(python-setuptools)
optdepends=('xclip: Support for X11'
			'wl-clipboard: Support for Wayland')
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/spyoungtech/pyclip/archive/refs/tags/v${pkgver}.tar.gz")
b2sums=('281a2dacd82d7501e01750134d82fc0b66ac1d41a631b9573160262c94cfb97ad463036e8ec523674580fdfb71849175e58836530d761462a72ba9ba3f2fd618')

build() {
	cd "${_pkgname}-${pkgver}"
	python setup.py build
}

package() {
	cd "${_pkgname}-${pkgver}"
	python setup.py install --skip-build --root="${pkgdir}" --optimize=1
	install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
