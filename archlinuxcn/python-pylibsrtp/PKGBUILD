# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=pylibsrtp
pkgname=python-pylibsrtp
pkgver=0.6.8
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
sha512sums=('c7901f91aa3710160021372d230c8d1a5a07b2c1dbc0987fdc9874356f01fffa76c12b87cd138acb20be4bd94df8d771c1de5feea0a32088f2a15af34a917d16')

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
