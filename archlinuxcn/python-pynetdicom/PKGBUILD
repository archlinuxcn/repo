# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-pynetdicom
_pkgname=pynetdicom
pkgver=3.0.3
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
sha512sums=('c2445ad854ffa227427202175b5d3ed1a0787454edb49cc04931205026abc799000f41b8eaafa7928bc47d33431c448124fef3647c4d21d98e55a894d1cea975')

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
