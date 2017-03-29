_pkgname=curio
pkgname=python-curio
pkgver=0.7
pkgrel=1
pkgdesc="Curio - Concurrent I/O"
arch=('any')
url="https://github.com/dabeaz/curio"
license=('BSD')
depends=('python')
makedepends=('python-setuptools')
source=('https://pypi.python.org/packages/09/c8/cdb6ebfea6e729b27497850538dcd6fa2611052409e9c7fb2cca3db8913d/curio-0.7.tar.gz')
md5sums=('df1ce58b5cb080c1520902855029d5f6')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
