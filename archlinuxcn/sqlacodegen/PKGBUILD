# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=sqlacodegen
_name=sqlacodegen
pkgver=3.0.0
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
sha512sums=('019d019ea25fee47d55b8344bc6274d26a8f39007a0eecf5985a439e0584594fb100f1323cf4de12bd6b277d55eba25d3dd4d7770790ddfcdc9aa592f2c138dc')

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
