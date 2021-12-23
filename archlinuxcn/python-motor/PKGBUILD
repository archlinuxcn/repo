# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=motor
pkgname=python-motor
pkgver=2.5.1
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
sha512sums=('6aad292f083e7121f11a85b021f5da143f4df1a9fcc06e19bed9ee6c470c6579765e5a39f2a0232f07feef3d9fe83e77c25045d4e981d0df18cbf972bac77588')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
# vim:set ts=2 sw=2 et:
