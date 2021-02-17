# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-dicomweb-client
_pkgname=dicomweb-client
pkgver=0.52.0
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
sha512sums=('cf8acd57bdeafbec0a5832cbe8dad5b1f94158ab3682e5542e2e4db5d6b8ea6e8e2d84e31661e14ea570b0cac52026a3ce860e34b8e6aae6a5c19a937866088d')

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
