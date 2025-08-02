# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-pynetdicom
_pkgname=pynetdicom
pkgver=3.0.4
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
sha512sums=('5f7cafb8abc3937cdc7156fec2105ad6740c1861cccb03c449a42b131ba5e97241d6341a8781533b55332885d6de34e6eeaecdfefc2a69ebe46c220a492bf98a')

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
