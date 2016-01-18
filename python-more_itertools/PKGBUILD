# Submitter: Germán Osella Massa <gosella@gmail.com>

pkgname=('python-more_itertools' 'python2-more_itertools')
pkgver=2.2
pkgrel=5
pkgdesc='More routines for operating on iterables, beyond itertools'
arch=('any')
url='https://pypi.python.org/pypi/more-itertools'
license=('MIT')
makedepends=('python-setuptools' 'python2-setuptools')
source=("https://pypi.python.org/packages/source/m/more-itertools/more-itertools-$pkgver.tar.gz")
md5sums=('b8d328a33f966bf40bb829bcf8da35ce')

package_python-more_itertools() {
  depends=('python')

  cd "$srcdir/more-itertools-$pkgver"
  rm -rf build
  python setup.py install --root="$pkgdir/" --optimize=1
}

package_python2-more_itertools() {
  depends=('python2')

  cd "$srcdir/more-itertools-$pkgver"
  rm -rf build
  python2 setup.py install --root="$pkgdir/" --optimize=1
}

# vim:set ts=2 sw=2 et:
