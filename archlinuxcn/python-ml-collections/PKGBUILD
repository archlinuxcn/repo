# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=ml_collections
pkgname=python-ml-collections
pkgver=0.1.1
pkgrel=1
pkgdesc='A library of Python Collections designed for ML use cases'
arch=('any')
url='https://github.com/google/ml_collections'
license=('Apache')
depends=(
  absl-py
  python-contextlib2
  python-six
  python-yaml
)
makedepends=(
  python-setuptools
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/google/ml_collections/archive/refs/tags/v${pkgver}.tar.gz")
sha512sums=('4ee02a53ab597acb2a239d0764412ad1f9a9959b8ab486ed18fc96837013a5a475bb73c1ee04419852af5f5ecdb7b4a33db36e4ec431d549c9fa2bc5934676d8')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
# vim:set ts=2 sw=2 et:
