_pkgname=memory_profiler
pkgname=python-memory_profiler
pkgver=0.41
pkgrel=1
pkgdesc="A module for monitoring memory usage of a python program"
arch=('any')
url="http://pypi.python.org/pypi/memory_profiler"
license=('BSD')
depends=('python' 'python-psutil' 'python-setuptools')
source=('https://pypi.python.org/packages/source/m/memory_profiler/memory_profiler-0.41.tar.gz')
md5sums=('8615aecbcc5cf1a761c819b9f4976cad')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"

  python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
