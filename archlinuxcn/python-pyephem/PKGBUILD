# Maintainer: Lukasz Pozarlik <lpozarlik at gmail dot com>
# Contributor: Masutu Subric <masutu dot arch at gmail dot com>
# Contributor: Michal Marek <reqamst at gmail dot com>

pkgname=('python-pyephem' 'python2-pyephem')
pkgver=4.1.1
pkgrel=1
pkgdesc="PyEphem provides scientific-grade astronomical computations"
arch=('i686' 'x86_64')
url="http://rhodesmill.org/pyephem/"
license=('GPL' 'LGPL')
makedepends=('python' 
  'python-setuptools' 
  'python2' 
  'python2-setuptools')
options=(!emptydirs)
source=("https://files.pythonhosted.org/packages/source/e/ephem/ephem-$pkgver.tar.gz")
md5sums=('2a3c3ada17e839ff55b02007f44dbb83')

build() {
  cp -r ${srcdir}/ephem-${pkgver} ${srcdir}/ephem-${pkgver}-py2

  cd ${srcdir}/ephem-${pkgver}
  python setup.py build

  cd ${srcdir}/ephem-${pkgver}-py2
  python2 setup.py build
}

package_python-pyephem() {
  depends=('python')
  cd "$srcdir/ephem-$pkgver"
  python setup.py install --root=$pkgdir/ --optimize=1
}

package_python2-pyephem() {
  depends=('python2')
  cd "$srcdir/ephem-$pkgver"
  python2 setup.py install --root=$pkgdir/ --optimize=1
}

