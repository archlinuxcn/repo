_pkgname=memory_profiler
pkgname=python-memory_profiler
pkgver=0.45
pkgrel=1
pkgdesc="A module for monitoring memory usage of a python program"
arch=('any')
url="http://pypi.python.org/pypi/memory_profiler"
license=('BSD')
depends=('python' 'python-psutil' 'python-setuptools')
source=('https://pypi.python.org/packages/e9/16/135a03bb71126cb8f097bb2789fb0c46e297a801995f051318fdd49631e2/memory_profiler-0.45.tar.gz')
md5sums=('ea76e5119071744655769fce566b27cf')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
