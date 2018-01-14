_pkgname=multio
pkgname=python-multio
pkgver=0.2.0
pkgrel=1
pkgdesc="mulio - an unified async library for curio and trio"
arch=('any')
url="https://github.com/theelous3/multio"
license=('MIT')
depends=('python' 'python-multio-provider')
makedepends=('python-setuptools')
source=('https://pypi.python.org/packages/7d/66/47b7d039433dab3660d0b6b34e0a9983f9574acd6fa60ebb4bda0e5b45aa/multio-0.2.0.tar.gz')
md5sums=('a1d22b322da2e9444aa036640986cc3e')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
