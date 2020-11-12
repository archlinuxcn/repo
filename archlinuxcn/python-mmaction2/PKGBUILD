# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=mmaction2
pkgname=python-mmaction2
pkgver=0.8.0
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
  python-setuptools
)
optdepends=(
  python-av
  python-onnx
  python-onnxruntime
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/open-mmlab/mmaction2/archive/v${pkgver}.tar.gz"
  "0001-fix-missing-__init__.py.patch::https://github.com/open-mmlab/mmaction2/pull/337.patch"
)
sha512sums=('4fbfb5e066b83c7c6d1480457c1fd4edbf32c3bd7f44c74a76d52b2d4b91d93ca05849e0356009585096cd664a7d433d5027448ea367a322dc65c541c097229e'
            'b8cdf38f45384f935763cd4438e8e8c9823a861c147c47f31e3273e1d199b57b25ef0791c92709f648d2febc1138af7189f6ed9f88abc61465ad30943a88867b')

prepare() {
  cd "${_pkgname}-${pkgver}"
  patch -p1 -i "${srcdir}/0001-fix-missing-__init__.py.patch"
  # uncomment this line to relax mmcv version requirement
  sed -i '10,13d' "mmaction/__init__.py"
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
