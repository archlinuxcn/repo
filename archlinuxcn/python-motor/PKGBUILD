# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=motor
pkgname=python-motor
pkgver=3.1.1
pkgrel=1
pkgdesc='The async Python driver for MongoDB and Tornado or asyncio'
arch=('any')
url='https://github.com/mongodb/motor'
license=('Apache')
depends=(
  python-pymongo
)
makedepends=(
  python-setuptools
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/mongodb/motor/archive/refs/tags/${pkgver}.tar.gz")
sha512sums=('49f31215a5e6e6e94c6b0e0b0deafa04a9b3a70de248115c3095cbfbb259d60655602cd82b0339937bfb7970d5ceabbf9073ea67b6354ee24cbbe93fd371e4b4')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
# vim:set ts=2 sw=2 et:
