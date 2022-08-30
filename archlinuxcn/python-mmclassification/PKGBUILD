# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=mmclassification
pkgname=python-mmclassification
pkgver=0.23.2
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
sha512sums=('8d23329ba20e8c0a7e4be6e5318a968d6304ce820a1b890522b31a3c5f2d9f1dd441045d0e86c713d812344cd0f92f47a4f49746cbc1a3762ac7a78b3e4be1a8')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
# vim:set ts=2 sw=2 et:
