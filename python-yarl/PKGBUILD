_pkgname=yarl
pkgname=python-yarl
pkgver=0.10.1
pkgrel=1
pkgdesc="Yet another URL library"
arch=('any')
url="https://github.com/aio-libs/yarl/"
license=('Apache')
depends=('python' 'python-multidict')
makedepends=('python-setuptools')
source=('https://pypi.python.org/packages/7b/70/1597b5f367d64742c4d6b3dc44d7c0e4d4f705e16e302ea7b92719c65dd0/yarl-0.10.1.tar.gz')
md5sums=('c08802c5e90038e360cd30160a3078eb')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
