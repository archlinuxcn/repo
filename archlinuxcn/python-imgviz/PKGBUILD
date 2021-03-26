# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=imgviz
pkgname=python-imgviz
pkgver=1.2.6
pkgrel=1
pkgdesc='Image Visualization Tools (object detection, semantic and instance segmentation)'
arch=('any')
url='https://github.com/wkentaro/imgviz'
license=('MIT')
depends=(
  python-matplotlib
  python-numpy
  python-pillow
  python-yaml
)
makedepends=(
  python-setuptools
)
checkdepends=(
  python-pytest
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/wkentaro/imgviz/archive/v${pkgver}.tar.gz")
sha512sums=('05338a613ecdcf2cecb202bd04e10d84c9c4cfd91ec646a46810d4b83721f2683e22d6fef936ab9f6941f6c40a4fe06c378b0c2e679abb284178a0389e86aaed')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

check() {
  cd "${_pkgname}-${pkgver}"
  PYTHONPATH="${PWD}/build/lib" pytest -v
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 "LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
