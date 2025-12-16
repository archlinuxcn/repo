# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-dicomweb-client
_pkgname=dicomweb-client
pkgver=0.60.1
pkgrel=2
pkgdesc='Python client for DICOMweb RESTful services'
arch=(any)
url='https://github.com/MGHComputationalPathology/dicomweb-client'
license=(MIT)
depends=(
  'python-numpy'
  'python-pillow'
  'python-pydicom'
  'python-requests'
  'python-retrying'
)

makedepends=(
  git
  python-build
  python-hatchling
  python-installer
  python-uv-dynamic-versioning
  python-wheel
)

source=("${_pkgname}::git+https://github.com/ImagingDataCommons/dicomweb-client.git#tag=v${pkgver}")
sha512sums=('cf08ddd7bd7ada80c86e89788b22b14ad76a92fc9d9bea975d233cd4c3001d04c78b9df56957614c087923b7a623b45375edf98b57e70ba5b1ab0b931ff10845')


build() {
  cd "${_pkgname}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
