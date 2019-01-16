_pkgname=asks
pkgname=python-asks
pkgver=2.2.0
pkgrel=1
pkgdesc="asks - async http"
arch=('any')
url="https://github.com/theelous3/asks"
license=('MIT')
depends=('python' 'python-multio' 'python-h11')
makedepends=('python-setuptools')
source=('https://files.pythonhosted.org/packages/56/c5/046c4d7d863d2a453698af7220803127750140c80fb8f8b4233b0501681b/asks-2.2.0.tar.gz')
md5sums=('a1709dd181ebc602a72b2a2d9b88971d')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
