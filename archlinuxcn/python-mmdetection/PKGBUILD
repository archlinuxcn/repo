# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=mmdetection
pkgname=python-mmdetection
pkgver=2.3.0
pkgrel=1
pkgdesc='OpenMMLab Detection Toolbox and Benchmark'
arch=('any')
url='https://github.com/open-mmlab/mmdetection'
license=('Apache')
depends=(
  python-mmcv
  python-numpy
  python-pycocotools-openmm
  python-pytorch
  python-terminaltables
  python-torchvision
)
makedepends=(
  python-setuptools
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/open-mmlab/mmdetection/archive/v${pkgver}.tar.gz")
sha512sums=('80a865d65f42e886e6a358702dc49d9df39f700069047d287e70647e81dbcf2b9d1fd27b2b01087b738b96a25c2251618dd8f4d59b7a428c621f6fbff79c6e02')

build() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
# vim:set ts=2 sw=2 et:
