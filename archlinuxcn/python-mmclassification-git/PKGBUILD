# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=mmclassification
pkgname=python-mmclassification-git
pkgver=0.22.0.r2.5a67bc8a
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
  git
  python-setuptools
)
optdepends=(
  python-albumentations
  python-colorama
  python-requests
  python-rich
)
provides=(python-mmclassification)
conflicts=(python-mmclassification)
source=("${_pkgname}::git+https://github.com/open-mmlab/mmclassification.git")
sha512sums=('SKIP')

pkgver() {
  cd "${_pkgname}"
  printf "%s" "$(git describe --long | sed 's/\([^-]*-\)g/r\1/;s/-/./g')" | sed "s/^v//"
}

build() {
  cd "${_pkgname}"
  python setup.py build
}

package() {
  cd "${_pkgname}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
# vim:set ts=2 sw=2 et:
