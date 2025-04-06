# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=pylibsrtp
pkgname=python-pylibsrtp
pkgver=0.12.0
pkgrel=1
pkgdesc='Python bindings for libsrtp'
arch=('x86_64')
url='https://github.com/aiortc/pylibsrtp'
license=('BSD-3-Clause')
depends=(
  glibc
  libsrtp
  python-cffi
)
makedepends=(
  python-build
  python-installer
  python-setuptools
  python-wheel
)

source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/aiortc/pylibsrtp/archive/refs/tags/${pkgver}.tar.gz")
sha512sums=('81b1a3f74d6117f406e2c4a7ba9035da2b9200bcc48bf7eb7f22a56ee731b0e6f007cd963af940ffaaead61fd595a45627a4fb95cdd99a282b5943e30585a01b')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
