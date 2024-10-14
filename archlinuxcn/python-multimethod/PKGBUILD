# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-multimethod
_pkgname=multimethod
pkgver=2.0rc1
pkgrel=1
pkgdesc='Multiple argument dispatching'
arch=('any')
url='https://github.com/coady/multimethod'
license=('Apache-2.0')
depends=(
  python
)
makedepends=(
  python-build
  python-installer
  python-setuptools
  python-wheel
)
checkdepends=(
  python-pytest
  python-pytest-cov
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/coady/multimethod/archive/v${pkgver}.tar.gz")
sha512sums=('2042b54688f12b6eee6510bd98af17318cc204e987fec6cdb4ee30dd5b7a3ac65e8bf70664ebd9ee73cbcec0733215603719520d7edab32e5d6402cace6abef9')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

check() {
  cd "${_pkgname}-${pkgver}"
  pytest -v --cov
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
}
# vim:set ts=2 sw=2 et:
