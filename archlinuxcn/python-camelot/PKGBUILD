# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=camelot
pkgname=python-camelot
pkgver=0.10.1
pkgrel=3
pkgdesc='A Python library to extract tabular data from PDFs'
arch=('any')
url='https://github.com/camelot-dev/camelot'
license=('MIT')
depends=(
  ghostscript
  python-chardet
  python-click
  python-pdfminer
  python-matplotlib
  python-numpy
  python-opencv
  python-openpyxl
  python-pandas
  python-pdfminer
  python-pdftopng
  python-pypdf2
  python-tabulate
  tk
)
makedepends=(
  python-setuptools
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/camelot-dev/camelot/archive/v${pkgver}.tar.gz"
  "0001.fix-pypdf-version.patch::https://github.com/camelot-dev/camelot/pull/307.patch"
)
sha512sums=('aeb1446021caccb0aa302d68d8ec17e0598debc29f0521d910c9a14c140a526d14ad8c749bac4fec4e366d8aeced2e9bc36aae1694f172ecbfeca351d97e848d'
            'dbef0511893cd333fb14c90ceaf16ddd46c09380cbe27b931b3cf8413f017491488b76a7069c9685a11a2d66924d9647945504f1af5c253855a829d4c17e804c')

prepare() {
  cd "${_pkgname}-${pkgver}"
  patch -p1 -i "${srcdir}/0001.fix-pypdf-version.patch"
  sed -i 's,isEncrypted,is_encrypted,g' camelot/handlers.py
  # python package name is renamed to `pypdf`
  sed -i 's,PyPDF2,pypdf,' camelot/handlers.py
}

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
