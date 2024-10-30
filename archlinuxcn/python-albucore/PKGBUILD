# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=albucore
pkgname=python-albucore
pkgver=0.0.20
pkgrel=1
pkgdesc='A high-performance image processing library designed to optimize and extend the Albumentations library with specialized functions for advanced image transformations'
arch=('any')
url='https://github.com/albumentations-team/albucore'
license=('MIT')
depends=(
  python-numpy
  python-opencv
  python-stringzilla
)
makedepends=(
  python-build
  python-installer
  python-setuptools
  python-wheel
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/albumentations-team/albucore/archive/refs/tags/${pkgver}.tar.gz")
sha512sums=('71303f3b3724edae28cd0cdd804277b95d8d52d058c5fcbb4237b1bc385a4ebbb9ba6ea8ef01aa73ad13edb20eba5ee5209a3a762c16d6290691936753cedd22')

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
