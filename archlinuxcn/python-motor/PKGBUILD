# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=motor
pkgname=python-motor
pkgver=3.3.0
pkgrel=1
pkgdesc='The async Python driver for MongoDB and Tornado or asyncio'
arch=('any')
url='https://github.com/mongodb/motor'
license=('Apache')
depends=(
  python-pymongo
)
makedepends=(
  python-build
  python-installer
  python-setuptools
  python-wheel
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/mongodb/motor/archive/refs/tags/${pkgver}.tar.gz")
sha512sums=('55f443d26179a0fee4b646a3689085c4383d680835d97027448ccc64b8256ab29277f51f2d199e5ad25cc2e3189f2a2a7a664139ee74fd2ae2dd6408ffaad7d4')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
}
# vim:set ts=2 sw=2 et:
