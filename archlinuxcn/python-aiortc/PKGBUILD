# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=aiortc
pkgname=python-aiortc
pkgver=1.3.1
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
sha512sums=('72290830203e117ef34e11776f43949236b369232e6b3b0cdc7c9a18b4350c1293040063babf6292a230c05a3b97eaf5dd90a458e9c967f2ad387beb9b20fc56')

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
