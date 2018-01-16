_pkgname=asks
pkgname=python-asks
pkgver=1.3.9
pkgrel=1
pkgdesc="asks - async http"
arch=('any')
url="https://github.com/theelous3/asks"
license=('MIT')
depends=('python' 'python-multio' 'python-h11')
makedepends=('python-setuptools')
source=('https://pypi.python.org/packages/bd/db/12bff14c41c6e4131005acf41e924ee110c4524a4f7751aeb551b57da8fd/asks-1.3.9.tar.gz')
md5sums=('937361180a3c485c6ab6ca45da3e5cb8')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
