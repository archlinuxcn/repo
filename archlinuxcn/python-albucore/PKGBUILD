# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=albucore
pkgname=python-albucore
pkgver=0.0.14
pkgrel=2
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
sha512sums=('82d9d63d24ec2e6b1a56aed583d4918cacfef02464b2522eac03a86b5ff3884805e1561abe5d3ed4f2e474f736fc47481530ac691e3251ac901c8359cc8020a5')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
}
# vim:set ts=2 sw=2 et:
