_pkgname=memory_profiler
pkgname=python-memory_profiler
pkgver=0.41
pkgrel=2
pkgdesc="A module for monitoring memory usage of a python program"
arch=('any')
url="http://pypi.python.org/pypi/memory_profiler"
license=('BSD')
depends=('python' 'python-psutil' 'python-setuptools')
source=('https://pypi.python.org/packages/df/d7/826bebacb980941fd02726d012c33051ac89c31064b43eb2f6fd4048209c/memory_profiler-0.41.tar.gz')
md5sums=('8615aecbcc5cf1a761c819b9f4976cad')

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
