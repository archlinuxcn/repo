# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-multimethod
_pkgname=multimethod
pkgver=1.10
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
sha512sums=('e360c480617f238c4d50ee16d29d19da9054d1ec96cd75b37f969cb2b96ce8f316a943b9f89906f16e909eac875fc636ea53e43c6c77d64caaa5723bc493315e')

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
