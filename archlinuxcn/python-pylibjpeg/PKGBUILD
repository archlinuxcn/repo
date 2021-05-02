# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=pylibjpeg
pkgname=python-pylibjpeg
pkgver=1.3.0
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
sha512sums=('133ff61fec6c19809b1769758349d59380fa30d9aea98d818d5f3caa8a4d83287ba5773f26eadd8d9daeaf821b21c7f7e925678661bbd7f5ed8457359ab319ec')

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
