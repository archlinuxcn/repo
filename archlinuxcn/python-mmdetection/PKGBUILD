# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=mmdetection
pkgname=python-mmdetection
pkgver=2.24.0
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
sha512sums=('be9bce4ea9c22818be25803238718111cbe72f1c8f6c063647bf3027579c378efe8d64a4ca0efe98ec6a195aea3f12ed4fee68ea19a822c7ceec2f3b7beb1a9a')


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
