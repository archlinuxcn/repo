# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=xtcocoapi
pkgname=python-xcocotools
pkgver=1.14
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
sha512sums=('e2c5a18287759fc3dff94845b71142f834e9e5c2e8f9bd682e959b7365b438ed922bfe0b487fb1ac50a9fdce1f0a3dac326646c2dcdbcffb75f528a5a5405997')

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
