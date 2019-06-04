# Maintainer: Rhinoceros <https://aur.archlinux.org/account/rhinoceros>
# Contributor: Abhishek Mudgal
# Contributor: Ivan Semkin (ivan at semkin dot ru)

_pkgname=vdf
pkgname=(python-vdf python2-vdf)
pkgver=3.1
pkgrel=1
pkgdesc="Library for working with Valve's VDF text format"
arch=('any')
url='https://github.com/ValvePython/vdf'
license=('MIT')
depends=()
makedepends=(python-setuptools)
checkdepends=(python python2 python-nose python-coverage python-mock python2-nose python2-coverage python2-mock)
source=("https://github.com/ValvePython/vdf/archive/v$pkgver.tar.gz")
sha256sums=('6f7e87e0d1921a170032720b3e1e3ce260170faada2ee606539cb4ab022f52a3')

check() {
  cd "$srcdir/$_pkgname-$pkgver"
  python setup.py test
  python2 setup.py test
}

package_python-vdf() {
  depends=(python)
  cd "$srcdir/$_pkgname-$pkgver"
  python setup.py install --optimize=1 --root="${pkgdir}/"
  install -D -m644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

package_python2-vdf() {
  depends=(python2)
  cd "$srcdir/$_pkgname-$pkgver"
  python2 setup.py install --optimize=1 --root="${pkgdir}/"
  install -D -m644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
