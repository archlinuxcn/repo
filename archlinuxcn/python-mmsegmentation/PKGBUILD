# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=mmsegmentation
pkgname=python-mmsegmentation
pkgver=0.12.0
pkgrel=1
pkgdesc='OpenMMLab Semantic Segmentation Toolbox and Benchmark'
arch=('any')
url='https://github.com/open-mmlab/mmsegmentation'
license=('Apache')
depends=(
  python-mmcv
  python-numpy
)
makedepends=(
  python-setuptools
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/open-mmlab/mmsegmentation/archive/v${pkgver}.tar.gz")
sha512sums=('a9fd534e851e11af228aa27b7fe24c283b3f0169e1d8bbec98b5193116e068b5baad916950e4098daf951aae8e196d9991d1c5be306697d6837066bffd1682af')

build() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
# vim:set ts=2 sw=2 et:
