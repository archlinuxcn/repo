# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=aiortc
pkgname=python-aiortc
pkgver=1.3.0
pkgrel=1
pkgdesc='WebRTC and ORTC implementation for Python using asyncio'
arch=('x86_64')
url='https://github.com/aiortc/aiortc'
license=('BSD')
depends=(
  python-aioice
  python-av
  python-cffi
  python-cryptography
  python-google-crc32c
  python-pyee
  python-pylibsrtp
)
makedepends=(
  python-setuptools
)

source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/aiortc/aiortc/archive/refs/tags/${pkgver}.tar.gz")
sha512sums=('ca2f5eecdc5470ddbee7c0b55a710e9307fc713a1c40503f52440ebcedb60ecdc2ca6ed1477fdde5235b17904ba8d18475adbf2834b6abe23bc597a285c3a549')

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
