# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-deid
_pkgname=deid
pkgver=0.1.16
pkgrel=1
pkgdesc='Best effort anonymization for medical images using python'
arch=(any)
url='https://github.com/pydicom/deid'
license=(MIT)
depends=(
  python-matplotlib
  python-pydicom
)
makedepends=(
  python-setuptools
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/pydicom/deid/archive/refs/tags/${pkgver}.tar.gz")
sha512sums=('3d19af8b2e921cdf7618f26562ff30f464944eb939a6bc6cf9fbbd9d7780a23a08155266b731d3ee1ecd10ee576819110b89f83238d2013c9d5d55c8645132cf')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
