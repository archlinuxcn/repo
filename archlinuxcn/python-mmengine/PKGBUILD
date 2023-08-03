# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=mmengine
pkgname=python-mmengine
pkgver=0.8.4
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
  python-build
  python-installer
  python-setuptools
  python-wheel
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/open-mmlab/mmengine/archive/refs/tags/v${pkgver}.tar.gz")
sha512sums=('a490da5ea009b2d943510d05e15fb99113600a943a14b2fc4804c8e52be53b799300c2a316086714ff50be0a646c535f73e6aaf96a8068b2d8b83717c9684812')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
}
# vim:set ts=2 sw=2 et:
