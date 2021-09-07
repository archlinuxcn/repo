# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=mmaction2
pkgname=python-mmaction2
pkgver=0.18.0
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
sha512sums=('531550e3e1db99d8da2db2578bb135bf43254969f8c1254db513ff19ab6040a3293ba3cdeb414f40b5608b25ecb2195dd9565be432c6495fabc7d949902094f0')

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
