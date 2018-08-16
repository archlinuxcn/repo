_pkgname=memory_profiler
pkgname=python-memory_profiler
pkgver=0.54.0
pkgrel=1
pkgdesc="A module for monitoring memory usage of a python program"
arch=('any')
url="http://pypi.python.org/pypi/memory_profiler"
license=('BSD')
depends=('python' 'python-psutil' 'python-setuptools')
source=('https://files.pythonhosted.org/packages/8c/e2/6cfd60b81de29c40ff0e19247c76f334975d62a362b52b4c2772e8f0cd7b/memory_profiler-0.54.0.tar.gz')
md5sums=('b5729a1a0fb5b512be63bcc7bbb1eb9d')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
