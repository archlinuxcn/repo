_pkgname=memory_profiler
pkgname=python-memory_profiler
pkgver=0.42
pkgrel=1
pkgdesc="A module for monitoring memory usage of a python program"
arch=('any')
url="http://pypi.python.org/pypi/memory_profiler"
license=('BSD')
depends=('python' 'python-psutil' 'python-setuptools')
source=('https://pypi.python.org/packages/d5/84/6311b59c16b33f60650d3682af309acf63f1703728af501bd449f2ed3a0b/memory_profiler-0.42.tar.gz')
md5sums=('1574b8297bf40dad55c35ca0f10b7e2e')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
