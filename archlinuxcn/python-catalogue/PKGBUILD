# Maintainer: Philip Goto <philip.goto@gmail.com>
# Contributor: Caltlgin Stsodaat <contact@fossdaily.xyz>
# Contributor: Chris Brendel <cdbrendel@gmail.com>

_pkgname=catalogue
pkgname="python-${_pkgname}"
pkgver=2.0.7
pkgrel=1
pkgdesc='Super lightweight function registries for your library'
arch=(any)
url='https://github.com/explosion/catalogue'
license=(MIT)
depends=(python)
makedepends=(python-setuptools)
source=("https://files.pythonhosted.org/packages/source/${_pkgname::1}/${_pkgname}/${_pkgname}-${pkgver}.tar.gz")
b2sums=('a14548ab9892dc84f34b256708009dccaa8f1e1f13538f12d7c06ad3f2eaf9c7fcceffb93ab63e6ebb2459ba9b6343ba87f1f89a59b12bec49a3c7df7fc159d6')

build() {
	cd "${_pkgname}-${pkgver}"
	python setup.py build
}

package() {
	cd "${_pkgname}-${pkgver}"
	python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
	install -Dvm644 'README.md' -t "${pkgdir}/usr/share/doc/${pkgname}"
	install -Dvm644 'LICENSE' -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
