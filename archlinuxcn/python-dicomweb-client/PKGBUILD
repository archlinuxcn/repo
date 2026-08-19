# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-dicomweb-client
_pkgname=dicomweb-client
pkgver=0.61.2
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
sha512sums=('29cca04aa4ef27222c64b6b1865f5d987fbc481f2e82d66538dfd9e475591a46cc5132fb6bb61f72fcc7e38c281264ae30e16236597889714a1532d1e41dcb47')


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
