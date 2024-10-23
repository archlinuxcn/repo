# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=albucore
pkgname=python-albucore
pkgver=0.0.19
pkgrel=1
pkgdesc='A high-performance image processing library designed to optimize and extend the Albumentations library with specialized functions for advanced image transformations'
arch=('any')
url='https://github.com/albumentations-team/albucore'
license=('MIT')
depends=(
  python-numpy
  python-opencv
)
makedepends=(
  python-build
  python-installer
  python-setuptools
  python-wheel
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/albumentations-team/albucore/archive/refs/tags/${pkgver}.tar.gz")
sha512sums=('e5b7474efcf5b33996541b943488c634a3072b472521db92743f3ba5648d2f4a73668dd4ddd51d4b093f8908064a2841364396bee983a3ad4a06246ecdab1c62')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
}
# vim:set ts=2 sw=2 et:
