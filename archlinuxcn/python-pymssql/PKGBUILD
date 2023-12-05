# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=pymssql
pkgname=python-pymssql
pkgver=2.2.11
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
  python-build
  python-installer
  python-setuptools
  python-setuptools-scm
  python-wheel
)
checkdepends=(
  python-gevent
  python-psutil
  python-pytest
  python-pytest-timeout
  python-sqlalchemy
)
source=("${_pkgname}-${pkgver}.tar.gz::https://files.pythonhosted.org/packages/source/${_pkgname::1}/${_pkgname}/${_pkgname}-${pkgver}.tar.gz"
        "0001.fix-setuptools-scm-version.patch"
)
sha512sums=('802d864897b8c713935569c87dc3415d1947c0e1593218661c1c546eb83935f152a52e8a1594006a89a875b9ce0203a9de2410dad18af058d6d22fe2eb698dc4'
            '1d2c5cc733e8bd80884f6b3d0d5c4b2a1e4abdfbb3e25332ac556a1194e8c6e330af5b35fc16804950e9f215b6a766118146500d29b569f3b7c80547a724b494')

prepare() {
  # quick fix for https://github.com/pymssql/pymssql/issues/869
  cd "${_pkgname}-${pkgver}"
  patch -p1 -i "${srcdir}/0001.fix-setuptools-scm-version.patch"
}

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
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
