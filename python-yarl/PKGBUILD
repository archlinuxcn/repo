_pkgname=yarl
pkgname=python-yarl
pkgver=0.9.8
pkgrel=1
pkgdesc="Yet another URL library"
arch=('any')
url="https://github.com/aio-libs/yarl/"
license=('Apache')
depends=('python' 'python-multidict')
makedepends=('python-setuptools')
source=('https://pypi.python.org/packages/66/2e/646e7da82260ad1dce86ebeed0befbd487941b7aa61ee2291fa47aa71bf4/yarl-0.9.8.tar.gz')
md5sums=('055d1386dfc269c37785508b07d82665')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
