_pkgname=trio
pkgname=python-trio
pkgver=0.3.0
pkgrel=1
pkgdesc="An async/await-native I/O library for humans and snake people"
arch=('any')
url="https://github.com/python-trio/trio"
license=('MIT')
depends=('python' 'python-attrs' 'python-sortedcontainers' 'python-idna' 'python-async_generator')
makedepends=('python-setuptools')
provides=('python-multio-provider')
source=('https://pypi.python.org/packages/8e/78/5b8db604f67977c5ef1fee97db375da4446dd01563078d69f351cbab592b/trio-0.3.0.tar.gz')
md5sums=('05687d28b0545c9d20b0438a03e96a8e')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
