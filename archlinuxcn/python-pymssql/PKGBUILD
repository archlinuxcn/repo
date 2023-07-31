# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=pymssql
pkgname=python-pymssql
pkgver=2.2.8
pkgrel=1
pkgdesc='A simple database interface for Python that builds on top of FreeTDS to provide a Python DB-API (PEP-249) interface to Microsoft SQL Server'
arch=('x86_64')
url='https://github.com/pymssql/pymssql'
license=('LGPL2.1')
depends=(
  freetds
)
makedepends=(
  cython
  python-pip
  python-setuptools
)
checkdepends=(
  python-gevent
  python-psutil
  python-pytest
  python-pytest-timeout
  python-sqlalchemy
)
source=("${_pkgname}-${pkgver}.tar.gz::https://files.pythonhosted.org/packages/source/${_pkgname::1}/${_pkgname}/${_pkgname}-${pkgver}.tar.gz")
sha512sums=('2b1ad380085d8978e7c6b4d6c0f6a1c61c8d7f97b0f8626586e916f8f1644284fcd04b8110a0ce4d8efc8f406cdb1ffa08f630ea2d1767d90887bf75eabaa22a')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

check() {
  local python_version=$(python -c 'import sys; print("".join(map(str, sys.version_info[:2])))')
  cd "${_pkgname}-${pkgver}"
  PYTHONPATH="${PWD}/build/lib.linux-${CARCH}-cpython-${python_version}" pytest -v
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
# vim:set ts=2 sw=2 et:
