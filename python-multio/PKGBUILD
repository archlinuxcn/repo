_pkgname=multio
pkgname=python-multio
pkgver=0.2.4
pkgrel=1
pkgdesc="multio - an unified async library for curio and trio"
arch=('any')
url="https://github.com/theelous3/multio"
license=('MIT')
depends=('python' 'python-multio-provider')
makedepends=('python-setuptools')
source=('https://files.pythonhosted.org/packages/2f/71/e3cc66826887a9f8e949c2052d574a436be75b7c1bf7b7bef0ee5d00fbf5/multio-0.2.4.tar.gz')
md5sums=('b204e2c38c3fd7bd0c2465cf379ec2e9')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
