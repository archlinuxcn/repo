_pkgname=curio
pkgname=python-curio
pkgver=0.8
pkgrel=2
pkgdesc="Curio - Concurrent I/O"
arch=('any')
url="https://github.com/dabeaz/curio"
license=('BSD')
depends=('python')
makedepends=('python-setuptools')
provides=('python-multio-provider')
source=('https://pypi.python.org/packages/cc/a9/9dcb972d6e07531c82e199aeafb78d814dfb6a759dc77548027c82ede553/curio-0.8.tar.gz')
md5sums=('9caa4844eaaa9cf3dab1e20145afe309')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
