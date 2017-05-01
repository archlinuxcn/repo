_pkgname=memory_profiler
pkgname=python-memory_profiler
pkgver=0.47
pkgrel=1
pkgdesc="A module for monitoring memory usage of a python program"
arch=('any')
url="http://pypi.python.org/pypi/memory_profiler"
license=('BSD')
depends=('python' 'python-psutil' 'python-setuptools')
source=('https://pypi.python.org/packages/bf/f0/15dc10cac0d8c56782e51d94855955664aa4f420eaa6291314bc3a0a52a3/memory_profiler-0.47.tar.gz')
md5sums=('ed340aaaa0c7118f2a4c5b4edec6da1e')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
