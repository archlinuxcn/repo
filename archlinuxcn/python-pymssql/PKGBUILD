# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=pymssql
pkgname=python-pymssql
pkgver=2.2.1
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
sha512sums=('d44fbe506d7daf3b5fc1dfa20b99814aa3ed025cf8e4e14097f53014bc21918e0969e15149fa93c39367a06567502be08bb673e30ebdf87d6fc2c30b01216b7c')

get_pyver() {
  python -c 'import sys; print(str(sys.version_info[0]) + "." + str(sys.version_info[1]))'
}

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

check() {
  cd "${_pkgname}-${pkgver}"
  PYTHONPATH="${PWD}/build/lib.linux-${CARCH}-$(get_pyver)" pytest -v
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
# vim:set ts=2 sw=2 et:
