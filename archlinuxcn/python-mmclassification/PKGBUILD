# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=mmclassification
pkgname=python-mmclassification
pkgver=0.24.1
pkgrel=1
pkgdesc='OpenMMLab Image Classification Toolbox and Benchmark'
arch=('any')
url='https://github.com/open-mmlab/mmclassification'
license=('Apache')
depends=(
  python-matplotlib
  python-mmcv
  python-numpy
  python-pytorch
)
makedepends=(
  python-setuptools
)
optdepends=(
  python-albumentations
  python-colorama
  python-requests
  python-rich
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/open-mmlab/mmclassification/archive/refs/tags/v${pkgver}.tar.gz")
sha512sums=('1656eeaa711690620c98433f357d3b0d08367ade9f8e3b7c7326a7dae8fbca1cdf4dce613f64bf84253d413b83a492ebb31cf3dc6efdf266dccf33c13b38bcd6')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
# vim:set ts=2 sw=2 et:
