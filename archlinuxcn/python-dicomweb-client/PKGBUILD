# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-dicomweb-client
_pkgname=dicomweb-client
pkgver=0.55.0
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
sha512sums=('7ca7a1d9b6a19cb2c29d621f9dd00d720bebeec351baf28f073be48a7f44a1e841cd08b73ce6df84e47b9e96745c91d8a91040bae1f2a20cb5924ca31aaf4e72')

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
