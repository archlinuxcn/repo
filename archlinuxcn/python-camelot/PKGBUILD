# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=camelot
pkgname=python-camelot
pkgver=1.0.9
pkgrel=1
pkgdesc='A Python library to extract tabular data from PDFs'
arch=('any')
url='https://github.com/camelot-dev/camelot'
license=('MIT')
depends=(
  ghostscript
  python-chardet
  python-click
  python-ghostscript
  python-matplotlib
  python-numpy
  python-opencv
  python-openpyxl
  python-pandas
  python-pdfminer
  python-pdftopng
  python-pypdf
  python-tabulate
  tk
)
makedepends=(
  python-build
  python-installer
  python-setuptools
  python-setuptools-scm
  python-wheel
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/camelot-dev/camelot/archive/v${pkgver}.tar.gz")
sha512sums=('6d67a3e5c13d32c99e19eccbf9f32e86b88b32b103a3a218d8dd0cbfd65f3943195bf9739770db90cb68ecaa0eefffb12f8a7a9afe52f0ae014831c5ce509d49')

build() {
  cd "${_pkgname}-${pkgver}"
  SETUPTOOLS_SCM_PRETEND_VERSION=${pkgver} \
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
