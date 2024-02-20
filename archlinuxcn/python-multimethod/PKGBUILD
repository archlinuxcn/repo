# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-multimethod
_pkgname=multimethod
pkgver=1.11.1
pkgrel=1
pkgdesc='Multiple argument dispatching'
arch=('any')
url='https://github.com/coady/multimethod'
license=('Apache')
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
sha512sums=('42e9ad97b002e4ffb1bddc95c3c9620f91f45b63b179b4a31fe13d0a5634371947e9e130c04a12eb2dc7b779b0b396999e7a208af2e1a598183827f6ca807041')

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
