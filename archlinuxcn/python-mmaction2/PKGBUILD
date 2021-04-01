# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=mmaction2
pkgname=python-mmaction2
pkgver=0.13.0
pkgrel=1
pkgdesc="OpenMMLab's Next Generation Action Understanding Toolbox and Benchmark"
arch=('any')
url='https://github.com/open-mmlab/mmaction2'
license=('Apache')
depends=(
  opencv
  python-matplotlib
  python-mmcv
  python-numpy
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
sha512sums=('b5c009f4a508bdba3ec5b3b9c3b2d783c5c0ac57316afc34c3ec35c4a77d9f5f33652bea91fb548a2fc8687416df161acf1273a74bc0c1bce57a2da20a2da2ca')

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
