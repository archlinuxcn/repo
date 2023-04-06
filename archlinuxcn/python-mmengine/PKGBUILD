# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=mmengine
pkgname=python-mmengine
pkgver=0.7.2
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
sha512sums=('7d8347ea8244b28c09ec2bbb92875254279690824dc28911aa0d7a049454f88386b052ce7dd04e0b429d8ef3e0e6dba019ae54b92460527f37f094c57d669c3f')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
}
# vim:set ts=2 sw=2 et:
