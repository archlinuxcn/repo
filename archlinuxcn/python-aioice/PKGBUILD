# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=aioice
pkgname=python-aioice
pkgver=0.7.6
pkgrel=1
pkgdesc='asyncio-based Interactive Connectivity Establishment (RFC 5245)'
arch=('any')
url='https://github.com/aiortc/aioice'
license=('BSD')
depends=(
  python-dnspython
  python-netifaces
)
makedepends=(
  python-setuptools
)

source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/aiortc/aioice/archive/refs/tags/${pkgver}.tar.gz")
sha512sums=('88aedf289bc9ec4e5e83109dda860c77cd79c6e56acbe88017a970fad341617a807235e3f001dc1540f52d0475ae207a611a7ade7b591a4c2b3c3e468011675a')

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
