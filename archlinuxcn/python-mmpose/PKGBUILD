# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=mmpose
pkgname=python-mmpose
pkgver=1.3.2
pkgrel=4
pkgdesc='OpenMMLab Pose Estimation Toolbox and Benchmark'
arch=('any')
url='https://github.com/open-mmlab/mmpose'
license=('Apache-2.0')
depends=(
  python-chumpy
  python-json-tricks
  python-matplotlib
  python-mmcv
  python-mmengine
  python-munkres
  python-numpy
  python-opencv
  python-pillow
  python-pytorch
  python-scipy
  python-six
  python-torchvision
  python-xtcocotools
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
sha512sums=('5ee586addcce42f6a47ae581828922da92014457d909e2af3c6795ccbf0e26abc20c98915b0955752b71dc32a3ae7efaf1a17f33d3780dda2bdaf3a9cf373013')

prepare() {
  sed -i "s/version=get_version()/version='$pkgver'/" "${srcdir}/${_pkgname}-${pkgver}/setup.py"
}

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  local site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
  # delete unused .mim and tests dir
  rm -rfv ${pkgdir}${site_packages}/tests
}
# vim:set ts=2 sw=2 et:
