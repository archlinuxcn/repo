# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=mmaction2
pkgname=python-mmaction2
pkgver=0.24.0
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
  python-decord
  python-lmdb
  python-imgaug
  python-onnx
  python-onnxruntime
  python-timm
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/open-mmlab/mmaction2/archive/v${pkgver}.tar.gz")
sha512sums=('a49e73d23ca39d2a8e39271bc1e5e47d5338e3f3ce230f8815ebd3c98fd397a3025ad076f17ad1128698a358ada98320b04737bcde5f7e907b3e96f8dbe96187')

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
