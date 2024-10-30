# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-multimethod
_pkgname=multimethod
pkgver=1.12
epoch=1
pkgrel=2
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
sha512sums=('9ea992760ab97a67cbbe1b7236c22df9b7fb8a48f3842007005005cfba735dcf91d64c3691ccbfdd9998afd7462b9063ec10342cdf0708de18195156db43e93c')

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
