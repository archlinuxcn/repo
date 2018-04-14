_pkgname=trio
pkgname=python-trio
pkgver=0.4.0
pkgrel=1
pkgdesc="An async/await-native I/O library for humans and snake people"
arch=('any')
url="https://github.com/python-trio/trio"
license=('MIT')
depends=('python' 'python-attrs' 'python-sortedcontainers' 'python-idna' 'python-async_generator')
makedepends=('python-setuptools')
provides=('python-multio-provider')
source=('https://pypi.python.org/packages/30/a7/df0e9d376a0d2e4a0e7c2ecb282242d9d4c1a07a558290e5e6d071546a6d/trio-0.4.0.tar.gz')
md5sums=('80553acbf89c9670f7a90f06c9c8d960')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
