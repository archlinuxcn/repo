_pkgname=memory_profiler
pkgname=python-memory_profiler
pkgver=0.52.0
pkgrel=1
pkgdesc="A module for monitoring memory usage of a python program"
arch=('any')
url="http://pypi.python.org/pypi/memory_profiler"
license=('BSD')
depends=('python' 'python-psutil' 'python-setuptools')
source=('https://pypi.python.org/packages/23/11/50a969d32a14cdec2cfd57bee2e67fd6f83715a04361ba230dbce562b9cb/memory_profiler-0.52.0.tar.gz')
md5sums=('72bdc09360762f17e52d462b993d7623')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
