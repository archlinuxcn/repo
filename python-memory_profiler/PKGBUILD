_pkgname=memory_profiler
pkgname=python-memory_profiler
pkgver=0.51.0
pkgrel=1
pkgdesc="A module for monitoring memory usage of a python program"
arch=('any')
url="http://pypi.python.org/pypi/memory_profiler"
license=('BSD')
depends=('python' 'python-psutil' 'python-setuptools')
source=('https://pypi.python.org/packages/43/3f/2ade3772a2a823058f63032c7cd208a60f13c6ea915b1ff17f76262f64ff/memory_profiler-0.51.0.tar.gz')
md5sums=('b346a8b5017a3a6fd8d6ca67c4801aa4')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
