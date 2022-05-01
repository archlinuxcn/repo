# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=mmpose
pkgname=python-mmpose
pkgver=0.25.1
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
sha512sums=('f1f4a6ec9b1bebccfb677e3690c0f81092bedb142e884dc44fabb2bcd0e6bc7ef577d78b51122c91cd65160c919afd80c226eb49cb89f0e6398b2abc8d080467')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
# vim:set ts=2 sw=2 et:
