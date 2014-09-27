# Maintainer: Andrzej Giniewicz <gginiu@gmail.com>

pkgname=pypy-funcsigs
pkgver=0.4
pkgrel=1
pkgdesc="Python function signatures from PEP362 for PyPy"
arch=('any')
url="http://funcsigs.readthedocs.org"
depends=('pypy')
makedepends=('pypy-setuptools')
license=('Apache')
options=(!libtool)
source=(https://pypi.python.org/packages/source/f/funcsigs/funcsigs-${pkgver}.tar.gz)
md5sums=('fb1d031f284233e09701f6db1281c2a5')

build() {
  cd "${srcdir}"/funcsigs-${pkgver}

  pypy setup.py build
}

package() {
  cd "${srcdir}"/funcsigs-${pkgver}

  pypy setup.py install --root="${pkgdir}" --optimize=1
}
