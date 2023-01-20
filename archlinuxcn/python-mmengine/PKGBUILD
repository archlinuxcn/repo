# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=mmengine
pkgname=python-mmengine
pkgver=0.5.0
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
sha512sums=('f2dfed80963156dcc202f16d4be789f97ee3b37d41f68f5830b6913eb53b8d82350698ea6fc654421d96b231ca9d97ef0e84de7ac0dad00d6604ee5a7c19c76d')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
# vim:set ts=2 sw=2 et:
