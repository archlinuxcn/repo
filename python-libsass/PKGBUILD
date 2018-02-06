_pkgname=libsass
pkgname=python-libsass
pkgver=0.13.7
pkgrel=1
pkgdesc="SASS for Python: A straightforward binding of libsass for Python."
arch=('x86_64')
url="https://sass.github.io/libsass-python/"
license=('MIT')
depends=('python' 'python-six' 'libsass' 'python-setuptools')
makedepends=('gcc')
source=('https://pypi.python.org/packages/bf/5e/9e75c0ca8b33a51768fcd32e29cbce00476edee2959b2107ea0a5ff7d831/libsass-0.13.7.tar.gz')
md5sums=('2a2be593ffc0f86f20d3e48ab19b0ada')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
