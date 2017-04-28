_pkgname=memory_profiler
pkgname=python-memory_profiler
pkgver=0.46
pkgrel=1
pkgdesc="A module for monitoring memory usage of a python program"
arch=('any')
url="http://pypi.python.org/pypi/memory_profiler"
license=('BSD')
depends=('python' 'python-psutil' 'python-setuptools')
source=('https://pypi.python.org/packages/79/af/ae75a982319d3ba56650f99b3dbaccdb54eec8f273d68b8f49df64f41f82/memory_profiler-0.46.tar.gz')
md5sums=('c6c212529bfb4dc083de31f027784c21')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
