# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=pymssql
pkgname=python-pymssql
pkgver=2.3.12
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
sha512sums=('a52a1a85e0a92f6df40c8c6fb5013a5695fe45854be6e66577fc66c3346d77296cd04a05a1b84d598a90aec9c86917ffdec4b1e502798a23d85041febb45a8d6')

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
