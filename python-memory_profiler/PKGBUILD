_pkgname=memory_profiler
pkgname=python-memory_profiler
pkgver=0.48.0
pkgrel=1
pkgdesc="A module for monitoring memory usage of a python program"
arch=('any')
url="http://pypi.python.org/pypi/memory_profiler"
license=('BSD')
depends=('python' 'python-psutil' 'python-setuptools')
source=('https://pypi.python.org/packages/9e/de/496b4f3066b89808386a1ac6f06026b57035b7a0a286a525bc9a241396cd/memory_profiler-0.48.0.tar.gz')
md5sums=('6451d56bf51ec0aef7e5ad187b718542')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
