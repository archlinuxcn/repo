# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=sqlacodegen
_name=sqlacodegen
pkgver=3.1.1
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
sha512sums=('dce3adf5dc3787cf773843ad7b0539fbd14a33b065bf4f8b9b4a9b83a9625008f0e114d5b5810bf0b3eaacb6a036f2d4f905c6d9f05ba0cba41be7e5d86f13a2')

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
