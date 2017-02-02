_pkgname=curio
pkgname=python-curio
pkgver=0.5
pkgrel=1
pkgdesc="Curio - Concurrent I/O"
arch=('any')
url="https://github.com/dabeaz/curio"
license=('BSD')
depends=('python')
makedepends=('python-setuptools')
source=('https://pypi.python.org/packages/02/32/d9380fc9f479528c7bffc1c7a1b2fa95d0319d0671bac0ece1a324abf4ed/curio-0.5.tar.gz')
md5sums=('731f99bfdf0bffe744a151996d34df3b')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
