_pkgname=trio
pkgname=python-trio
pkgver=0.2.0
pkgrel=1
pkgdesc="An async/await-native I/O library for humans and snake people"
arch=('any')
url="https://github.com/python-trio/trio"
license=('MIT')
depends=('python' 'python-attrs' 'python-sortedcontainers' 'python-idna' 'python-async_generator')
makedepends=('python-setuptools')
source=('https://pypi.python.org/packages/c2/0f/9c435e994419f863538f175f6dfa3041a14eb4681d0f09e8417fb949bf27/trio-0.2.0.tar.gz')
md5sums=('5189606a0863fe5fc7d48ac06cd6fccd')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
