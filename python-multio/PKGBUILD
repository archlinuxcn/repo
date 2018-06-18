_pkgname=multio
pkgname=python-multio
pkgver=0.2.3
pkgrel=1
pkgdesc="multio - an unified async library for curio and trio"
arch=('any')
url="https://github.com/theelous3/multio"
license=('MIT')
depends=('python' 'python-multio-provider')
makedepends=('python-setuptools')
source=('https://files.pythonhosted.org/packages/af/3b/c074da0bb2175b508bfb354c020475b2089498f5fc91c1df8b7fecbac525/multio-0.2.3.tar.gz')
md5sums=('b9964647a546f1fe4e4fe6b2bc95b90e')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
