# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-cx-oracle
_name=cx_Oracle
pkgver=8.2.0
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
sha512sums=('c249d136abaad6c97ddbb2c6cc56aa5b5b1f0aa80aedb236617ca95c5ca50fb1e0cf31e5f11e80a8f674b217ef57f6a16a43c494b47e04d6f8845171ad77a38c')

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
