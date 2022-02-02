# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=pylibsrtp
pkgname=python-pylibsrtp
pkgver=0.7.1
pkgrel=1
pkgdesc='Python bindings for libsrtp'
arch=('x86_64')
url='https://github.com/aiortc/pylibsrtp'
license=('BSD')
depends=(
  libsrtp
  python-cffi
)
makedepends=(
  python-setuptools
)

source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/aiortc/pylibsrtp/archive/refs/tags/${pkgver}.tar.gz")
sha512sums=('ace4337240846b4837855a01a3a651c5785f043283465376ad5c95935d5a36f30ee5f07f7e7019dfc5c828c80748b2aeeb4f52a50ffea6bf4f425508fdf81c99')

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
