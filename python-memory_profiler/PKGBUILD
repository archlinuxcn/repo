_pkgname=memory_profiler
pkgname=python-$_pkgname
pkgver=0.32
pkgrel=2
pkgdesc="A module for monitoring memory usage of a python program"
arch=('any')
url="http://pypi.python.org/pypi/memory_profiler"
license=('Simplified')
depends=('python' 'python-psutil' 'python-setuptools')
source=('https://pypi.python.org/packages/source/m/memory_profiler/memory_profiler-0.32.tar.gz')
md5sums=('c65310467e05d8db4b10fa65534f3e5d')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"

  python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
