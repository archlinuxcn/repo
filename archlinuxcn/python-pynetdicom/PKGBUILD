# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-pynetdicom
_pkgname=pynetdicom
pkgver=3.0.1
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
sha512sums=('2cdcbdfef534e0ac44722eb3c687a17591a1b42df6a7d55dcc6f22c8e97427dd6bf07df613a8a1ad3393f9bf1edb65480cd39bd9d29047c8f88f43ea1ddf4103')

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
