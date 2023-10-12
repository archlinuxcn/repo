# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=mmpose
pkgname=python-mmpose
pkgver=1.2.0
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
  python-build
  python-installer
  python-setuptools
  python-wheel
)
optdepends=(
  python-albumentations
  python-onnx
  python-onnxruntime
  python-requests
  python-trimesh
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/open-mmlab/mmpose/archive/refs/tags/v${pkgver}.tar.gz")
sha512sums=('f30ad6a17b2c7f4f2b74472b13bbbbedcfa4ed4bfe24684f81fcc5d07a2ea1c9da70bf0b118ecfcfdc6ab609e1e75f7343c9f65e2205c41208552a271330f3d1')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  local site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
  # delete unused .mim and tests dir
  rm -rfv "${pkgdir}${site_packages}/mmpose/.mim"
  rm -rfv ${pkgdir}${site_packages}/tests
}
# vim:set ts=2 sw=2 et:
