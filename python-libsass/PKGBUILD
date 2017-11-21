_pkgname=libsass
pkgname=python-libsass
pkgver=0.13.4
pkgrel=1
pkgdesc="SASS for Python: A straightforward binding of libsass for Python."
arch=('x86_64')
url="http://hongminhee.org/libsass-python/"
license=('MIT')
depends=('python' 'python-six' 'libsass' 'python-setuptools')
makedepends=('gcc')
source=('https://pypi.python.org/packages/d9/ea/d2d67633f2d808bfa2461f54f7068fd21f47eb0980132e560cdcc99a7882/libsass-0.13.4.tar.gz')
md5sums=('a6bc47e45ef3f532867edc8d2cf166b2')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
