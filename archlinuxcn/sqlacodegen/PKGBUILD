# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=sqlacodegen
_name=sqlacodegen
pkgver=3.1.0
pkgrel=1
pkgdesc='Automatic model code generator for SQLAlchemy'
arch=(any)
url='https://github.com/agronholm/sqlacodegen'
license=(MIT)
depends=(
  python-inflect
  python-sqlalchemy
)
makedepends=(
  python-build
  python-installer
  python-setuptools
  python-setuptools-scm
  python-wheel
)

source=("${pkgname}-${pkgver}.tar.gz::https://github.com/agronholm/sqlacodegen/archive/refs/tags/${pkgver}.tar.gz")
sha512sums=('fb0c8907c66e849ea8e1bfb6c86f9685ebcb23a9f9bdb8c7ba471bc56c9de2627449e39e3fd301c29d52b2191d5de8ffad5187bf5dba856b50f43e1e7e308723')

build() {
  cd "${_name}-${pkgver}"
  SETUPTOOLS_SCM_PRETEND_VERSION=${pkgver} python -m build --wheel --no-isolation
}

package() {
  cd "${_name}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
