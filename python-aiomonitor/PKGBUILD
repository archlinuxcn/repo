_pkgname=aiomonitor
pkgname=python-aiomonitor
pkgver=0.3.1
pkgrel=1
pkgdesc="aiomonitor adds monitor and python REPL capabilities for asyncio application"
arch=('any')
url="https://github.com/aio-libs/aiomonitor"
license=('Apache')
depends=('python' 'python-aioconsole' 'python-terminaltables' 'python-setuptools')
source=('https://files.pythonhosted.org/packages/4c/e4/6314fe522d0c17fd01e14297e3ec58d4f4d2cf7bf1089590e1d23bc7653b/aiomonitor-0.3.1.tar.gz')
md5sums=('449c5868d494e14643441d1a6fcd25ea')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
