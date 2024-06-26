# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=motor
pkgname=python-motor
pkgver=3.5.0
pkgrel=1
pkgdesc='The async Python driver for MongoDB and Tornado or asyncio'
arch=('any')
url='https://github.com/mongodb/motor'
license=('Apache-2.0')
depends=(
  python-pymongo
)
makedepends=(
  python-build
  python-hatch-requirements-txt
  python-hatchling
  python-installer
  python-wheel
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/mongodb/motor/archive/refs/tags/${pkgver}.tar.gz")
sha512sums=('45f127fe401c9e4fdbb1ed2aa618d0f50533381eb9f169c1f0489fd61484294a23eb2bfdb814e7b26395092035366efaee8096722e4bb3c565ebd6ead6d0305f')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
}
# vim:set ts=2 sw=2 et:
