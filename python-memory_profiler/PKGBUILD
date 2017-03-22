_pkgname=memory_profiler
pkgname=python-memory_profiler
pkgver=0.44
pkgrel=1
pkgdesc="A module for monitoring memory usage of a python program"
arch=('any')
url="http://pypi.python.org/pypi/memory_profiler"
license=('BSD')
depends=('python' 'python-psutil' 'python-setuptools')
source=('https://pypi.python.org/packages/1a/ed/3d6dd57bd668f9a54ddf1dcc2c25766f7a1ebcedcd3127ad9ca96bb5956d/memory_profiler-0.44.tar.gz')
md5sums=('c03efb0fdf8338032e936ecb125c563b')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
