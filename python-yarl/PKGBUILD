_pkgname=yarl
pkgname=python-yarl
pkgver=0.9.2
pkgrel=1
pkgdesc="Yet another URL library"
arch=('any')
url="https://github.com/aio-libs/yarl/"
license=('Apache')
depends=('python' 'python-multidict')
makedepends=('python-setuptools')
source=('https://pypi.python.org/packages/4a/15/a9f1b82bb88c2c11fee12d0e4248f0ed4cb0ec3e2b25fa4b0e52baff0899/yarl-0.9.2.tar.gz')
md5sums=('09fc2fe4fcd34e9f49081c80efdd5a12')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
