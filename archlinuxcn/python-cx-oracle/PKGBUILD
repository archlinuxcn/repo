# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-cx-oracle
_name=cx_Oracle
pkgver=8.2.1
pkgrel=1
pkgdesc='Python interface to Oracle Database conforming to the Python DB API 2.0 specification'
arch=('x86_64')
url='https://oracle.github.io/python-cx_Oracle'
license=('BSD')
depends=(
  oracle-instantclient-basic
  python
)
makedepends=(
  python-setuptools
)
source=(
  "${_name}-${pkgver}.tar.gz::https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.tar.gz"
)
sha512sums=('879f25323ea037499c773be860d7c9a4f9bc675f7107a79a1ac027db45f6a4d71b47579b656fba267b85dacb76316f012de238ffda66ea33395ce5989b982116')

build() {
  cd "${srcdir}/${_name}-${pkgver}"
  python setup.py build
}

package() {
  cd "${srcdir}/${_name}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 "LICENSE.txt" -t "${pkgdir}/usr/share/licenses/${pkgname}"
  rm -rfv "${pkgname}/usr/cx_Oracle-doc"
}
# vim:set ts=2 sw=2 et:
