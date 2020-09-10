# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=mmdetection
pkgname=python-mmdetection
pkgver=2.4.0
pkgrel=2
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
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/open-mmlab/mmdetection/archive/v${pkgver}.tar.gz")
sha512sums=('22cfb7d806a92f4a9522cccf084748c0a96f85935c630c003779f32b0bd1b57ac52d8e540c4c8e98dedbfd1ced43c7081b10c8ed1a6618c1ea274570c2879552')


prepare() {
  cd "${_pkgname}-${pkgver}"
  # uncomment this line to relax mmcv version requirement
  #sed -i '23,26d' "mmdet/__init__.py"
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
