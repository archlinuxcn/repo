_pkgname=memory_profiler
pkgname=python-memory_profiler
pkgver=0.43
pkgrel=1
pkgdesc="A module for monitoring memory usage of a python program"
arch=('any')
url="http://pypi.python.org/pypi/memory_profiler"
license=('BSD')
depends=('python' 'python-psutil' 'python-setuptools')
source=('https://pypi.python.org/packages/ac/71/cb4cdac45861d7497e3bd6500b49fccfe5a3f2e57ba69933cba74abfef37/memory_profiler-0.43.tar.gz')
md5sums=('7b6cf03cbee3ad7f366261831282651a')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
