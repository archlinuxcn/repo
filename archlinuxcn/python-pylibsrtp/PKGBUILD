# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=pylibsrtp
pkgname=python-pylibsrtp
pkgver=0.7.0
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
sha512sums=('9bde47957b3ca9e568f165d5a488fdeda298ef2623bb936e588780d3b13fff382f826c27e589cb4049c47bdf5ff3aafe1e1393bfb3a609669257e501f0480bc7')

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
