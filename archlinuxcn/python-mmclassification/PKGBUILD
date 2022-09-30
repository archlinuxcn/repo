# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=mmclassification
pkgname=python-mmclassification
pkgver=0.24.0
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
sha512sums=('cb5a2c5ee89be9bee9b15accd482ed4ba8464b87c2616d935fcd3312290b58c1a9c6bfaeac76444b6e04c48d230bcd7874f24ecbb1a9e574017326723a3ab841')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
# vim:set ts=2 sw=2 et:
