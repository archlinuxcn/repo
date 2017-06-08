_pkgname=libsass
pkgname=python-libsass
pkgver=0.13.0
pkgrel=1
pkgdesc="SASS for Python: A straightforward binding of libsass for Python."
arch=('x86_64')
url="http://hongminhee.org/libsass-python/"
license=('MIT')
depends=('python' 'python-six' 'libsass' 'python-setuptools')
makedepends=('gcc')
source=('https://pypi.python.org/packages/cc/0b/efd232d304f04164f0b0ed74eea12736af33154aeb9fd29ea1b0c24fc49f/libsass-0.13.0.tar.gz')
md5sums=('b14ee54fdb12408a641172028a64c769')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
