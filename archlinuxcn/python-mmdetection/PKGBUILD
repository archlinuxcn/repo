# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=mmdetection
pkgname=python-mmdetection
pkgver=2.24.1
pkgrel=1
pkgdesc='OpenMMLab Detection Toolbox and Benchmark'
arch=('any')
url='https://github.com/open-mmlab/mmdetection'
license=('Apache')
depends=(
  python-mmcv
  python-numpy
  python-mmpycocotools
  python-pytorch
  python-terminaltables
  python-torchvision
)
makedepends=(
  python-pip
  python-setuptools
)
optdepends=(
  python-albumentations
  python-cityscapesscripts
  python-imagecorruptions
  python-mmlvis
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/open-mmlab/mmdetection/archive/v${pkgver}.tar.gz")
sha512sums=('24caeab0aff3975caf77c8da8839d33276541e4af791e21ea330e6e4c8f597b9b0c25f90716888bfd12447868ad8e09ff85715bf36084f8ab777b04070bdba9e')


prepare() {
  cd "${_pkgname}-${pkgver}"
  # uncomment this line to relax mmcv version requirement
  #sed -i '23,26d' "mmdet/__init__.py"
}

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
# vim:set ts=2 sw=2 et:
