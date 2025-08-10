# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=camelot
pkgname=python-camelot
pkgver=1.0.2
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
sha512sums=('7d600b486ad4a5affc5a735ce8ffe82b6e7d790c2b2e4803f69eb6f2d0aecef568e4b467364e7045d0ca85005de29feef678ca1e53beef5686abd8553679d1ea')

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
