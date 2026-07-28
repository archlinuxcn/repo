# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-dicomweb-client
_pkgname=dicomweb-client
pkgver=0.61.1
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
sha512sums=('ab7bfbfc4556a904e71391bdc8d336d1c4b14efa15b9d10d2b082fa7589a75fa3ad30cd74637063044ba54e36ca7f83ecbca79ee9a15a45e1130bc7a64eb31be')


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
