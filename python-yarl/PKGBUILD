_pkgname=yarl
pkgname=python-yarl
pkgver=0.8.0
pkgrel=1
pkgdesc="Yet another URL library"
arch=('any')
url="https://github.com/aio-libs/yarl/"
license=('Apache')
depends=('python' 'python-multidict')
makedepends=('python-setuptools')
source=('https://pypi.python.org/packages/ca/95/aa0cf9d3398038398c29616f744ed05cad26ab0d6f35a3569c26ad5bf349/yarl-0.8.0.tar.gz')
md5sums=('c5090f0ee08156276a7af298abc1c5eb')

export LANG=en_US.UTF-8

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"

  python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
