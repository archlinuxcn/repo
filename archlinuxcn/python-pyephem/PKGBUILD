# Maintainer: Lukasz Pozarlik <lpozarlik at gmail dot com>
# Contributor: Masutu Subric <masutu dot arch at gmail dot com>
# Contributor: Michal Marek <reqamst at gmail dot com>

pkgname=('python-pyephem')
pkgver=4.1.5
pkgrel=1
pkgdesc="PyEphem provides scientific-grade astronomical computations"
arch=('i686' 'x86_64')
url="http://rhodesmill.org/pyephem/"
license=('GPL' 'LGPL')
makedepends=('python' 
  'python-setuptools')
options=(!emptydirs)
source=("https://files.pythonhosted.org/packages/source/e/ephem/ephem-$pkgver.tar.gz")
md5sums=('943b29d8c47f884d90bea35c8a5b632d')

build() {
  cd ${srcdir}/ephem-${pkgver}
  python setup.py build
}

package_python-pyephem() {
  depends=('python')
  cd "$srcdir/ephem-$pkgver"
  python setup.py install --root=$pkgdir/ --optimize=1
}

