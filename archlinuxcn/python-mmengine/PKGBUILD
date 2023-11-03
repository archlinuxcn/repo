# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=mmengine
pkgname=python-mmengine
pkgver=0.9.1
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
sha512sums=('8cbdf2abdfcef765d226267902cc1447e1b4df2969362830de8e2c95aca34ec77b9dde6787a0c8f1896b3b5ccab8ef9f25451a96420ed8980246c7b20448cba0')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
}
# vim:set ts=2 sw=2 et:
