# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=mmengine
pkgname=python-mmengine
pkgver=0.4.0
pkgrel=1
pkgdesc='OpenMMLab Foundational Library for Training Deep Learning Models'
arch=('any')
url='https://github.com/open-mmlab/mmengine'
license=('Apache')
depends=(
  python-addict
  python-matplotlib
  python-numpy
  python-termcolor
  python-yaml
  yapf
)
makedepends=(
  python-setuptools
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/open-mmlab/mmengine/archive/refs/tags/v${pkgver}.tar.gz")
sha512sums=('9333a9758c197d7aa130771ba99717b76178f48fa5359f59a776f5bd61f0d3651e29887c77fd1a1f2c579e9607a6ae67f52f1ebb24911e24554c4b5821edc8e5')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
# vim:set ts=2 sw=2 et:
