# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-dicomweb-client
_pkgname=dicomweb-client
pkgver=0.61.0
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
sha512sums=('426196f396bfdb10730e550c603d0159bd7bce1811af8d55ee1b0bbf56c58d0e8a96a297fa36f96dc0a6a804660fdf00e53c6983f4945b81471315eda26e1b4f')


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
