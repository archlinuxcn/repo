_pkgname=asks
pkgname=python-asks
pkgver=1.3.8
pkgrel=3
pkgdesc="asks - async http"
arch=('any')
url="https://github.com/theelous3/asks"
license=('MIT')
depends=('python' 'python-multio' 'python-h11')
makedepends=('python-setuptools')
source=('https://pypi.python.org/packages/bb/8f/042ca93614a1f62e02ae5e0bff224c39a53762f224226ad12370c65ac6c5/asks-1.3.8.tar.gz')
md5sums=('8c0a8133aec1d006ba5ebda0e1862bcf')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
