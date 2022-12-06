# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=mmclassification
pkgname=python-mmclassification
pkgver=0.25.0
pkgrel=1
pkgdesc='OpenMMLab Image Classification Toolbox and Benchmark'
arch=('any')
url='https://github.com/open-mmlab/mmclassification'
license=('Apache')
depends=(
  python-matplotlib
  python-mmcv
  python-numpy
  python-pytorch
)
makedepends=(
  python-setuptools
)
optdepends=(
  python-albumentations
  python-colorama
  python-requests
  python-rich
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/open-mmlab/mmclassification/archive/refs/tags/v${pkgver}.tar.gz")
sha512sums=('6900ed1c8b08b3e1afba907bc5f78a2529021ef2b7de47d8ffba188103a8e823bd5928c72550f7289ee121036c0d1f457eadd1015b2c4e2cdc7578e96a55310e')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
# vim:set ts=2 sw=2 et:
