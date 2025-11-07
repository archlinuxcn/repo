# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=pymssql
pkgname=python-pymssql
pkgver=2.3.9
pkgrel=1
pkgdesc='DB-API (PEP-249) interface to Microsoft SQL Server'
arch=('x86_64')
url='https://github.com/pymssql/pymssql'
license=('LGPL-2.1-or-later')
depends=(
  freetds
  glibc
)
makedepends=(
  cython
  python-build
  python-installer
  python-setuptools
  python-setuptools-scm
  python-tomli
  python-wheel
)
checkdepends=(
  python-gevent
  python-psutil
  python-pytest
  python-pytest-timeout
  python-sqlalchemy
)
source=("${_pkgname}-${pkgver}.tar.gz::https://files.pythonhosted.org/packages/source/${_pkgname::1}/${_pkgname}/${_pkgname}-${pkgver}.tar.gz")
sha512sums=('f3e6ef22eb6142bdd804074169f35257b1eaa21a0db879af51a072df4a8d47a764deaa0ed094b8223541508f58857030e9b0b3bd734ff19858b51cfca5e66caa')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation -x
}

check() {
  local python_version=$(python -c 'import sys; print("".join(map(str, sys.version_info[:2])))')
  cd "${_pkgname}-${pkgver}"
  PYTHONPATH="${PWD}/build/lib.linux-${CARCH}-cpython-${python_version}" pytest -v
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
}
# vim:set ts=2 sw=2 et:
