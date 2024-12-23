# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=mmpretrain
pkgname=python-mmpretrain
pkgver=1.2.0
pkgrel=4
pkgdesc='OpenMMLab Pre-training Toolbox and Benchmark'
arch=('any')
url='https://github.com/open-mmlab/mmpretrain'
license=('Apache-2.0')
depends=(
  python-einops
  python-matplotlib
  python-mmcv
  python-model-index
  python-numpy
  python-rich
  python-pytorch
)
makedepends=(
  python-build
  python-installer
  python-setuptools
  python-wheel
)
optdepends=(
  python-albumentations
  python-scikit-learn
  python-grad-cam
  python-requests
)
provides=(
  python-mmclassification
)
replaces=(
  python-mmclassification
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/open-mmlab/mmpretrain/archive/refs/tags/v${pkgver}.tar.gz")
sha512sums=('47c76769657219e7baf3d2d1d645489691b5172b1a67b1cb82cc000c1fd34277381f6ea406fc1bf2164ed2edbca28cc6d65a69a94f4293d86c5e6fa2eafffe8a')

prepare() {
  sed -i "s/version=get_version()/version='$pkgver'/" "${_pkgname}-${pkgver}/setup.py"
}

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
}
# vim:set ts=2 sw=2 et:
