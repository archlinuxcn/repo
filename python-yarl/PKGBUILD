_pkgname=yarl
pkgname=python-yarl
pkgver=0.9.6
pkgrel=1
pkgdesc="Yet another URL library"
arch=('any')
url="https://github.com/aio-libs/yarl/"
license=('Apache')
depends=('python' 'python-multidict')
makedepends=('python-setuptools')
source=('https://pypi.python.org/packages/2f/08/b197bd19930410d647939af91cc3a26125b826a2d7b22bf28c3ccad79819/yarl-0.9.6.tar.gz')
md5sums=('6a359ac0e24cdf287e3d461966cc481a')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
