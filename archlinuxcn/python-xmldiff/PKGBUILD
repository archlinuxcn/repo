# Maintainer: Puqns67 <me@puqns67.icu>
# Contributor: Guillaume Horel <guillaume.horel@gmail.com>
# Contributor: Caleb Maclennan <caleb@alerque.com>

_name='xmldiff'
pkgname="python-${_name}"
pkgver=2.6.3
pkgrel=2
pkgdesc='A libray and command line utility for diffing xml'
url="https://github.com/Shoobx/xmldiff"
license=('MIT')
arch=('any')
depends=('python' 'python-lxml' 'python-setuptools')
makedepends=('python-build' 'python-installer' 'python-wheel')

source=("${_name}-${pkgver}.tar.gz"::"${url}/archive/refs/tags/${pkgver}.tar.gz")

b2sums=('7fc6e19bae7904301cfa5048d4fa7ad757bab000c50975acf8261107b8224558abfdf9d95935404c26e09cf616bacbc4f3deefd7a9e600ff0ec9d22100ba64b1')

build() {
	cd "${srcdir}/${_name}-${pkgver}"
	python -m build --wheel --no-isolation
}

check() {
	cd "${srcdir}/${_name}-${pkgver}"
	python -m unittest
}

package() {
	cd "${srcdir}/${_name}-${pkgver}"
	python -m installer --destdir="${pkgdir}" dist/*.whl
	install -Dm644 "${srcdir}/${_name}-${pkgver}/LICENSE.txt" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE" 
}
