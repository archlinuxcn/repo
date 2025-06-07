# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=albucore
pkgname=python-albucore
pkgver=0.0.25
pkgrel=1
pkgdesc='A high-performance image processing library designed to optimize and extend the Albumentations library with specialized functions for advanced image transformations'
arch=('any')
url='https://github.com/albumentations-team/albucore'
license=('MIT')
depends=(
  python-numpy
  python-opencv
  python-simsimd
  python-stringzilla
)
makedepends=(
  python-build
  python-installer
  python-setuptools
  python-wheel
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/albumentations-team/albucore/archive/refs/tags/${pkgver}.tar.gz")
sha512sums=('9489e6158f0283a73ec2cad1a40a25800bce7e49ef7b1f9b2b2c1eaf2e659f571283f05842bd64b03597866717a87efa196b10196c3bc9973445eed561855ee4')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
