# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=sqlacodegen
_name=sqlacodegen
pkgver=3.0.0rc4
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
sha512sums=('d096c93645e06c0949b845438d0540412cd4fcc913a0b669a4d3503dba070846b9ea74d13c8a1c6909ac895f5615212b904348a696bde2569f2d7a64a6cef47e')

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
