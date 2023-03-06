# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=sqlacodegen
_name=sqlacodegen
pkgver=2.3.0.post1
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
  python-setuptools
  python-pip
)
checkdepends=(
  python-mysql-connector
  python-psycopg2
  python-pytest
  python-pytest-cov
)

source=("${pkgname}-${pkgver}.tar.gz::https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.tar.gz")
sha512sums=('6a888f57b584da1b318212582879bf0d03b9770432b4bc97a6eeb7a8671f1e365a55c4ca3b509c568ac44064201c8033a5e13ebcb8bb5d853c37001276d0b419')

build() {
  cd "${_name}-${pkgver}"
  python setup.py build
}

check() {
  cd "${_name}-${pkgver}"
  PYTHONPATH="${PWD}/build/lib" pytest -v .
}

package() {
  cd "${_name}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
