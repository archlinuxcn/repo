_pkgname=curio
pkgname=python-curio
pkgver=0.9
pkgrel=1
pkgdesc="Curio - Concurrent I/O"
arch=('any')
url="https://github.com/dabeaz/curio"
license=('BSD')
depends=('python')
makedepends=('python-setuptools')
provides=('python-multio-provider')
source=('https://pypi.python.org/packages/e4/61/6e7daab81d17c47296c63c346d794c29e95218a7bceba88bf4a57cf7bb27/curio-0.9.tar.gz')
md5sums=('48dd49df3fabe06a6a787ce3ba9f9ad5')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
