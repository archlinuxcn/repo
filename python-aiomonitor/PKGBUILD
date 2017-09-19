_pkgname=aiomonitor
pkgname=python-aiomonitor
pkgver=0.3.0
pkgrel=1
pkgdesc="aiomonitor adds monitor and python REPL capabilities for asyncio application"
arch=('any')
url="https://github.com/aio-libs/aiomonitor"
license=('Apache')
depends=('python' 'python-aioconsole' 'python-terminaltables' 'python-setuptools')
source=('https://pypi.python.org/packages/9f/7a/f9b021cbf88ff66d1652006146d443cfa63ba8574cbf97d4d6ff4adfa766/aiomonitor-0.3.0.tar.gz')
md5sums=('446319b270c81f1d3839f89858b2fa40')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
