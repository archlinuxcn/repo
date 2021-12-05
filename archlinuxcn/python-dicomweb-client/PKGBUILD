# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-dicomweb-client
_pkgname=dicomweb-client
pkgver=0.54.2
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
sha512sums=('331be5c495e5b038a0746b5cd893de8615fcd1e8f9bba3f40366b6bbe0fec2c5250815e4b6597f39fe97ebb602176a2cc3e8624e75336a4cba51c5b2ffd80e9b')

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
