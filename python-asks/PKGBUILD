_pkgname=asks
pkgname=python-asks
pkgver=2.0.0
pkgrel=1
pkgdesc="asks - async http"
arch=('any')
url="https://github.com/theelous3/asks"
license=('MIT')
depends=('python' 'python-multio' 'python-h11')
makedepends=('python-setuptools')
source=('https://files.pythonhosted.org/packages/cd/02/89b66b69d9cd539ca10ebb8434960b79187d829ed071a41844cb8b913938/asks-2.0.0.tar.gz')
md5sums=('6f741f2c0a81df3109723f821224393a')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
