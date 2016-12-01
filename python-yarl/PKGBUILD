_pkgname=yarl
pkgname=python-yarl
pkgver=0.7.1
pkgrel=1
pkgdesc="Yet another URL library"
arch=('any')
url="https://github.com/aio-libs/yarl/"
license=('Apache')
depends=('python' 'python-multidict')
makedepends=('python-setuptools')
source=('https://pypi.python.org/packages/e6/d1/0de27bc2350e679ac0f241f6641f75229e5b88ae8a7a0f2b8f79c871afca/yarl-0.7.1.tar.gz')
md5sums=('265b20d6844bb17aa89134c568abe5b6')

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
