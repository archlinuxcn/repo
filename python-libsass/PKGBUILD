_pkgname=libsass
pkgname=python-libsass
pkgver=0.14.2
pkgrel=1
pkgdesc="Sass for Python: A straightforward binding of libsass for Python."
arch=('x86_64')
url="https://sass.github.io/libsass-python/"
license=('MIT')
depends=('python' 'python-six' 'libsass' 'python-setuptools')
makedepends=('gcc')
source=('https://pypi.python.org/packages/0f/a3/c2aed4128ee3639653da412a1b1e7ae95804a5fa7dbd35d4fb3593f6f0a8/libsass-0.14.2.tar.gz')
md5sums=('1da0fbd2be44045e349907535106db4a')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
