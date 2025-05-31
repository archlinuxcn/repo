# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-pynetdicom
_pkgname=pynetdicom
pkgver=3.0.0
pkgrel=1
pkgdesc='A Python implementation of the DICOM networking protocol'
arch=(any)
url='https://github.com/pydicom/pynetdicom'
license=(MIT)
depends=(
  python-pydicom
)
makedepends=(
  python-build
  python-flit-core
  python-installer
  python-poetry-core
  python-wheel
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/pydicom/pynetdicom/archive/refs/tags/v${pkgver}.tar.gz")
sha512sums=('9d7d39805ed6c5f7f53dfbf8dc58083a7310103f924741435a28cbc843cf47bb1fc27e2398005ab4b0d758c4b008e9ae44580a8c24ee4707b68d59004a774305')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm644 LICENCE -t "${pkgdir}/usr/share/licenses/${pkgname}"
  # avoid file conflicts with dcmtk, add pynetdicom prefix
  for i in "${pkgdir}/usr/bin"/*; do
    mv -vf "$i" "${pkgdir}/usr/bin/pynetdicom-$(basename "$i")"
  done
}
# vim:set ts=2 sw=2 et:
