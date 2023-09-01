# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=motor
pkgname=python-motor
pkgver=3.3.1
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
sha512sums=('07749d0db563e56ed36e3547d5733c485dead885bc098e2fd57359d21758af6d075cffbf39bd42a056c55aff27d8b93c4c3d5989f11d26f2dedc616697a4e9ef')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
}
# vim:set ts=2 sw=2 et:
