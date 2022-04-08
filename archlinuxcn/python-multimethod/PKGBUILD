# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-multimethod
_pkgname=multimethod
pkgver=1.8
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
sha512sums=('433a2c72a6c98129df70aa09d1e640f2f23be6c42236cb88ad4ef9dee89406a9b6a2c01771b2b7e69ffa8d6b6cae05a8e0cd273d77c2eed86c5b8ee0c6887c8c')

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
