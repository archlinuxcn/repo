# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=mmaction2
pkgname=python-mmaction2
pkgver=1.2.0
pkgrel=5
pkgdesc="OpenMMLab's Next Generation Action Understanding Toolbox and Benchmark"
arch=('any')
url='https://github.com/open-mmlab/mmaction2'
license=('Apache-2.0')
depends=(
  python-matplotlib
  python-mmcv
  python-numpy
  python-opencv
  python-pillow
  python-pytorch
  python-scipy
  python-torchvision
)
makedepends=(
  python-build
  python-installer
  python-setuptools
  python-wheel
)
optdepends=(
  python-av
  python-decord
  python-lmdb
  python-imgaug
  python-onnx
  python-onnxruntime
  python-timm
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/open-mmlab/mmaction2/archive/v${pkgver}.tar.gz")
sha512sums=('ccedf843db145971a61ecaea23d6334d4d27896b9506200734b29f331efbb52cd551a23b8c9d68398f4c1930a62cdd8b370200c7934fe9acb38de6069965811e')

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
}
# vim:set ts=2 sw=2 et:
