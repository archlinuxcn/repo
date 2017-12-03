_pkgname=memory_profiler
pkgname=python-memory_profiler
pkgver=0.50.0
pkgrel=1
pkgdesc="A module for monitoring memory usage of a python program"
arch=('any')
url="http://pypi.python.org/pypi/memory_profiler"
license=('BSD')
depends=('python' 'python-psutil' 'python-setuptools')
source=('https://pypi.python.org/packages/8e/16/f2f08cdbd7791dd200bd6de933b5aff9dcf7ffb2e6d22506cdafb4fc5b74/memory_profiler-0.50.0.tar.gz')
md5sums=('75288aff9c14c5444db990a6c39c50d8')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
