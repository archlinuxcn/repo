_pkgname=curio
pkgname=python-curio
pkgver=0.1
pkgrel=1
pkgdesc="Curio - Concurrent I/O"
arch=('any')
url="https://github.com/dabeaz/curio"
license=('BSD')
depends=('python' 'python-setuptools')
source=('https://pypi.python.org/packages/source/c/curio/curio-0.1.tar.gz')
md5sums=('cc667ad56947843f6326b61b099e8609')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"

  python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
