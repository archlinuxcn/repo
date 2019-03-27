# Maintainer: Abhishek Mudgal
# Contributor: Ivan Semkin (ivan at semkin dot ru)

_pkgname=vdf
pkgname=(python-vdf python2-vdf)
pkgver=3.0
pkgrel=2
pkgdesc="Library for working with Valve's VDF text format"
arch=('any')
url='https://github.com/ValvePython/vdf'
license=('MIT')
depends=()
makedepends=(python-setuptools)
checkdepends=(python python2 python-nose python-coverage python-mock python2-nose python2-coverage python2-mock)
source=("https://github.com/ValvePython/vdf/archive/v$pkgver.tar.gz")
sha256sums=('f15b9a1ab7ad11c53c002c407a125520e5f0f61e54ab1cf6c5ab06e7a18c9592')

check() {
  cd "$srcdir/$_pkgname-$pkgver"
  python setup.py test
  python2 setup.py test
}

package_python-vdf() {
  depends=(python)
  cd "$srcdir/$_pkgname-$pkgver"
  python setup.py install --optimize=1 --root="${pkgdir}/"
}

package_python2-vdf() {
  depends=(python2)
  cd "$srcdir/$_pkgname-$pkgver"
  python2 setup.py install --optimize=1 --root="${pkgdir}/"
}
# vim:set ts=2 sw=2 et:
