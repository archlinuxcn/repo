_pkgname=libsass
pkgname=python-libsass
pkgver=0.14.3
pkgrel=1
pkgdesc="Sass for Python: A straightforward binding of libsass for Python."
arch=('x86_64')
url="https://sass.github.io/libsass-python/"
license=('MIT')
depends=('python' 'python-six' 'libsass' 'python-setuptools')
makedepends=('gcc')
source=('https://files.pythonhosted.org/packages/3e/7e/d412288ee1d3643aa889e2b409f65175f41cf14f08a2d24be354ec090b25/libsass-0.14.3.tar.gz')
md5sums=('6dc78da2121d0fda5838293c41af541b')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
