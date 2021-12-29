# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-pynetdicom
_pkgname=pynetdicom
pkgver=2.0.1
pkgrel=1
pkgdesc='A Python implementation of the DICOM networking protocol'
arch=(any)
url='https://github.com/pydicom/pynetdicom'
license=(MIT)
depends=(
  python-pydicom
)
makedepends=(
  python-setuptools
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/pydicom/pynetdicom/archive/refs/tags/v${pkgver}.tar.gz")
sha512sums=('1e9e67a4d9adce2416d577876054181b84a605ea2a0fecb37e0bd17bd7cb69b7e7de6a17b4fb11543970d1a78952a5905af57c4da0f0b7f8efc74a866832d268')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 LICENCE.txt -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
