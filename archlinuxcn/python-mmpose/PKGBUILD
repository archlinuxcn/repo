# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=mmpose
pkgname=python-mmpose
pkgver=1.3.0
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
sha512sums=('87b4292d8e08eed699b2e2198e82c8a613b724cbca778e169757b2b63d3fc3479e40f098feafda261acc0c8e9bc427a5c8920e8f61c665bf48ff586dabb90390')

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
