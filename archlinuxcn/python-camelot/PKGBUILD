# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=camelot
pkgname=python-camelot
pkgver=0.9.0
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
sha512sums=('3bbf2c70d542a4e5bd2aeb0e360dd84462b793ea723c3f6d1ca9fde12fdcbf305385c8d4bda5786c2f44776204714bf9ea98a15a7d540d211f28d04121ccb8a8')

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
