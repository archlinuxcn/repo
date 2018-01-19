_pkgname=libsass
pkgname=python-libsass
pkgver=0.13.6
pkgrel=1
pkgdesc="SASS for Python: A straightforward binding of libsass for Python."
arch=('x86_64')
url="https://sass.github.io/libsass-python/"
license=('MIT')
depends=('python' 'python-six' 'libsass' 'python-setuptools')
makedepends=('gcc')
source=('https://pypi.python.org/packages/15/f1/335d99c84148d2d1857d489b53f34466bfcba77e882d717ba2a517812326/libsass-0.13.6.tar.gz')
md5sums=('89e70b7c12495c59b1b9b57d5ae59825')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
