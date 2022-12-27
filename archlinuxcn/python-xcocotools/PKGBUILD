# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=xtcocoapi
pkgname=python-xcocotools
pkgver=1.13
pkgrel=1
pkgdesc='Extended COCO-API'
arch=('x86_64')
url='https://github.com/jin-s13/xtcocoapi'
license=('MIT')
depends=(
  python-numpy
  python-matplotlib
)
makedepends=(
  cython
  python-setuptools
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/jin-s13/xtcocoapi/archive/refs/tags/v${pkgver}.tar.gz")
sha512sums=('32d68ee387e4833a6b86f50809b9a61f4bcbb4bbfec5b377e13cce1588b10a4ceabe8cb3d4367d9be4ae25306a450ad99a24bb42657c85bf3b91c56c9588c3c6')

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
