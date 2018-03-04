_pkgname=multio
pkgname=python-multio
pkgver=0.2.1
pkgrel=1
pkgdesc="multio - an unified async library for curio and trio"
arch=('any')
url="https://github.com/theelous3/multio"
license=('MIT')
depends=('python' 'python-multio-provider')
makedepends=('python-setuptools')
source=('https://pypi.python.org/packages/57/c7/85f4912482474e94d9d60ab0db3334aa9bc3075ef4d4dcfd48edb82a54fb/multio-0.2.1.tar.gz')
md5sums=('c9a7321fbcbfb4081c5523477735bc69')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
