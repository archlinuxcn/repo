# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=camelot
pkgname=python-camelot
pkgver=0.8.2
pkgrel=1
pkgdesc='A Python library to extract tabular data from PDFs'
arch=('any')
url='https://github.com/camelot-dev/camelot'
license=('MIT')
depends=(
  ghostscript
  opencv
  python-chardet
  python-click
  python-matplotlib
  python-numpy
  python-openpyxl
  python-pandas
  python-pdfminer
  python-pypdf2
  tk
)
makedepends=(
  python-setuptools
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/camelot-dev/camelot/archive/v${pkgver}.tar.gz")
sha512sums=('1ba36125ca727473923c8704004bfb0136d611cc3044e883bd78f875ccf8ad64a45883260344a383d02efc801900a451413b1c3cdc680a95903c4d681c7f3382')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
