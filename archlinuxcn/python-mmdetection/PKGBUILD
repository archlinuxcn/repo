# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=mmdetection
pkgname=python-mmdetection
pkgver=2.3.0
pkgrel=6
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
optdepends=(
  python-albumentations
  python-cityscapesscripts
  python-imagecorruptions
  python-lvis-openmm
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/open-mmlab/mmdetection/archive/v${pkgver}.tar.gz"
"0001-fix-ClassBalancedDataset.patch::https://github.com/open-mmlab/mmdetection/pull/3577.patch")
sha512sums=('80a865d65f42e886e6a358702dc49d9df39f700069047d287e70647e81dbcf2b9d1fd27b2b01087b738b96a25c2251618dd8f4d59b7a428c621f6fbff79c6e02'
            '1bf79e840d7d38c781163699559fa47d9881e6615f316c8a188244fce1660a22d2255bc07956aacb929d1b0abaff3d2c1a636dfcabedf4de06a43eedd216fe2a')


prepare() {
  cd "${_pkgname}-${pkgver}"
  patch -p1 -i ../0001-fix-ClassBalancedDataset.patch
  # relax mmcv version requirement
  sed -i '23,26d' "mmdet/__init__.py"
}

build() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
# vim:set ts=2 sw=2 et:
