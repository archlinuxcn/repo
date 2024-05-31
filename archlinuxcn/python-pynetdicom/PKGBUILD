# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-pynetdicom
_pkgname=pynetdicom
pkgver=2.1.0
pkgrel=2
pkgdesc='A Python implementation of the DICOM networking protocol'
arch=(any)
url='https://github.com/pydicom/pynetdicom'
license=(MIT)
depends=(
  python-pydicom
)
makedepends=(
  python-build
  python-installer
  python-poetry-core
  python-wheel
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/pydicom/pynetdicom/archive/refs/tags/v${pkgver}.tar.gz")
sha512sums=('3aae8b4e332c81d5e53303b97fa3fc4ee78c72b236910fdaadb28b97a7ce69eb32aa6f5ad012a1021615ab684a28514d9df2bda08d5148b60856cde16a6e4ebb')

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
