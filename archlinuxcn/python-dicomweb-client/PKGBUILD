# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-dicomweb-client
_pkgname=dicomweb-client
pkgver=0.50.2
pkgrel=1
pkgdesc='Python client for DICOMweb RESTful services'
arch=(any)
url='https://github.com/MGHComputationalPathology/dicomweb-client'
license=(MIT)
depends=(
  'python-numpy'
  'python-pillow'
  'python-pydicom'
  'python-requests'
  'python-six'
)

makedepends=(
  'python-setuptools'
)

source=("${pkgname}-${pkgver}.tar.gz::https://github.com/MGHComputationalPathology/dicomweb-client/archive/v${pkgver}.tar.gz")
sha512sums=('f2d39963b1426b4512f44a0de37f8e526db68c0b9f3008e046f5305b1685269b3e0ed9cec3b3bd0a01239b9436d84abe2dcc92d7611b4a6bdbf9d8ae19847d3a')

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
