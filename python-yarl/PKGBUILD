_pkgname=yarl
pkgname=python-yarl
pkgver=0.9.5
pkgrel=1
pkgdesc="Yet another URL library"
arch=('any')
url="https://github.com/aio-libs/yarl/"
license=('Apache')
depends=('python' 'python-multidict')
makedepends=('python-setuptools')
source=('https://pypi.python.org/packages/7f/56/729e64437b23c30069b8bf924e06f058e1d1f7ab8629412c1a9202fb6e32/yarl-0.9.5.tar.gz')
md5sums=('875660b3c2d811c55ae801f1a86c01f9')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
