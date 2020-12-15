# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=pylibjpeg
pkgname=python-pylibjpeg
pkgver=1.1.1
pkgrel=1
pkgdesc='A Python framework for decoding JPEG images, with a focus on supporting pydicom'
arch=(any)
url='https://github.com/pydicom/pylibjpeg'
license=(MIT)
depends=(
  python-pylibjpeg-openjpeg
)
makedepends=(
  python-setuptools
)
checkdepends=(
  python-pytest
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/pydicom/pylibjpeg/archive/v${pkgver}.tar.gz")
sha512sums=('ac62f66dc7e74e8e8c7c781fb370a7869058efd28ebdbf7a75f569c3a82d543d5d7b3405262ffca4a134c92dfe1e65c2c03c510e34bd2d7982a51c7b5ce8e113')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 "LICENCE.txt" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
