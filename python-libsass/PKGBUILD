_pkgname=libsass
pkgname=python-libsass
pkgver=0.13.3
pkgrel=1
pkgdesc="SASS for Python: A straightforward binding of libsass for Python."
arch=('x86_64')
url="http://hongminhee.org/libsass-python/"
license=('MIT')
depends=('python' 'python-six' 'libsass' 'python-setuptools')
makedepends=('gcc')
source=('https://pypi.python.org/packages/4a/e5/ba98c8ce05d88a75054546c6bc785c0f779be8eb41fd973185af6c7d35b2/libsass-0.13.3.tar.gz')
md5sums=('3c11bed144fdd8d6339a6e89a7ceafae')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
