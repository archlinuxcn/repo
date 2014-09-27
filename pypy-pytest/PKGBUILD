pkgbase=pypy-pytest
pkgname=('pypy3-pytest' 'pypy-pytest')
pkgver=2.6.0
pkgrel=1
pkgdesc="Simple powerful testing with Python"
arch=('any')
license=('MIT')
url="http://pytest.org/"
makedepends=('pypy3-setuptools' 'pypy-setuptools' 'pypy3-py' 'pypy-py')
source=("http://pypi.python.org/packages/source/p/pytest/pytest-$pkgver.tar.gz")
sha512sums=('c5a4b8fdf178832a05fe97259e0ae110c06547c7783c513fd8f631b1f4cc2d63def10beb05243c01a328e69576604560b6becd42d61c6226f9bff7ea5492fa33')

prepare() {
  cp -r pytest-${pkgver}{,-py2}
}

build() {
  cd "$srcdir/pytest-${pkgver}"
  pypy3 setup.py build

  cd "$srcdir/pytest-${pkgver}-py2"
  pypy setup.py build
}

package_pypy3-pytest() {
  depends=("pypy3>=2.3" "pypy3<=2.4" 'pypy3-py' 'pypy3-setuptools')

  cd pytest-${pkgver}
  pypy3 setup.py install --root="${pkgdir}" --optimize=1
  install -D -m644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"

  install -dm755 "${pkgdir}/usr/bin"
  ln -s "/opt/pypy3/bin/py.test" "${pkgdir}/usr/bin/pypy.test3"
}

package_pypy-pytest() {
  depends=('pypy' 'pypy-py' 'pypy-setuptools')

  cd pytest-${pkgver}-py2
  pypy setup.py install --root="${pkgdir}" --optimize=1
  install -D -m644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"

  install -dm755 "${pkgdir}/usr/bin"
  ln -s "/opt/pypy/bin/py.test" "${pkgdir}/usr/bin/pypy.test"
}
