pkgbase=pypy-py
pkgname=('pypy3-py' 'pypy-py')
pkgver=1.4.22
pkgrel=1
pkgdesc="library with cross-python path, ini-parsing, io, code, log facilities"
arch=('any')
license=('MIT')
url="http://pylib.readthedocs.org/en/latest/"
makedepends=('pypy-setuptools' 'pypy3-setuptools')
source=("http://pypi.python.org/packages/source/p/py/py-$pkgver.tar.gz")
sha512sums=('3cbc75257a7de345f0f23b6374a542608392d05f6600ba8ab743eea4fc46cc88ccaa829c1e2370eabb9892fbef8a16df9f5eb7956571d6f2b465a75817f70d7a')

prepare() {
  cp -a py-${pkgver}{,-py2}
}

build() {
  cd "$srcdir/py-${pkgver}"
  pypy3 setup.py build

  cd "$srcdir/py-${pkgver}-py2"
  pypy setup.py build
}

package_pypy3-py() {
  depends=("pypy3>=2.3" "pypy3<=2.4")

  cd py-${pkgver}
  pypy3 setup.py install --root="${pkgdir}" --optimize=1
  install -D -m644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

package_pypy-py() {
  depends=('pypy')

  cd py-${pkgver}-py2
  pypy setup.py install --root="${pkgdir}" --optimize=1
  install -D -m644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
