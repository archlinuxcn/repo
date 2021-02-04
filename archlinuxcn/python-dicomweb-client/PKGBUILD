# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-dicomweb-client
_pkgname=dicomweb-client
pkgver=0.51.0
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
sha512sums=('43dc3d8963da25497e1ea682f52eef19d23dd16f79e42192b290f70381c1656891863832d1495350c80811d82267bd30ea810e0bf97014a6ed43bffeea60d500')

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
