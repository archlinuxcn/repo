# Maintainer: Felix Yan <felixonmars@gmail.com>

pkgname=python2-pint
pkgver=0.5.2
pkgrel=1
pkgdesc="A unit library for Python"
depends=('python2')
makedepends=('python2-setuptools')
source=("https://pypi.python.org/packages/source/P/Pint/Pint-${pkgver}.zip")
url="http://pint.readthedocs.org"
license=('BSD')
arch=('any')
md5sums=('0b380f9ae5f20d502246b2c7c3a74107')

package() {
  cd "${srcdir}/Pint-${pkgver}"
  python2 setup.py install --root="${pkgdir}" --optimize=1
}
