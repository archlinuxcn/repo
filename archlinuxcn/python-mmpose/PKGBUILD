# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=mmpose
pkgname=python-mmpose
pkgver=0.28.0
pkgrel=1
pkgdesc='OpenMMLab Pose Estimation Toolbox and Benchmark'
arch=('any')
url='https://github.com/open-mmlab/mmpose'
license=('Apache')
depends=(
  python-chumpy
  python-json-tricks
  python-matplotlib
  python-mmcv
  python-munkres
  python-numpy
  python-opencv
  python-pillow
  python-pytorch
  python-torchvision
  python-xcocotools
)
makedepends=(
  python-pip
  python-setuptools
)
optdepends=(
  python-albumentations
  python-onnx
  python-onnxruntime
  python-requests
  python-trimesh
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/open-mmlab/mmpose/archive/refs/tags/v${pkgver}.tar.gz")
sha512sums=('236ab512a3c036c150f3acf068d33be505757d735e665ed4d01af71f5015bd9479301ceb9a28c2c434e01bdb545fdba2f8d9149cf70578b3f7b60b67976a5f29')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
# vim:set ts=2 sw=2 et:
