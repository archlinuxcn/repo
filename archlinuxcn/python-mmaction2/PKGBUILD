# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=mmaction2
pkgname=python-mmaction2
pkgver=0.22.0
pkgrel=1
pkgdesc="OpenMMLab's Next Generation Action Understanding Toolbox and Benchmark"
arch=('any')
url='https://github.com/open-mmlab/mmaction2'
license=('Apache')
depends=(
  python-matplotlib
  python-mmcv
  python-numpy
  python-opencv
  python-pillow
  python-pytorch
  python-torchvision
)
makedepends=(
  python-pip
  python-setuptools
)
optdepends=(
  python-av
  python-onnx
  python-onnxruntime
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/open-mmlab/mmaction2/archive/v${pkgver}.tar.gz")
sha512sums=('778a8eee7b1e884a056bb2fa9dccc456646e4c64a3e0b844e1bf5b6366ea13304b67ca485db01f8d7c8e5333e45a4fd63c384992bee00eba8d5cd24ef7010f2d')

prepare() {
  cd "${_pkgname}-${pkgver}"
  # uncomment this line to relax mmcv version requirement
  # sed -i '10,13d' "mmaction/__init__.py"
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
