# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=camelot
pkgname=python-camelot
pkgver=0.10.1
pkgrel=4
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
  python-setuptools
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/camelot-dev/camelot/archive/v${pkgver}.tar.gz"
  "0001.fix-pypdf-version.patch::https://github.com/camelot-dev/camelot/pull/307.patch"
)
sha512sums=('aeb1446021caccb0aa302d68d8ec17e0598debc29f0521d910c9a14c140a526d14ad8c749bac4fec4e366d8aeced2e9bc36aae1694f172ecbfeca351d97e848d'
            '7f65d245bf54581cd9a8774780bc2f5af4126399e1f9db443d6f2f110ca3d15d8532bbd10d07b3001f2cf617d2951ff0d50491ffc1dc2b75766a5ffd8cf20bd7')

prepare() {
  cd "${_pkgname}-${pkgver}"
  patch -p1 -i "${srcdir}/0001.fix-pypdf-version.patch"
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
