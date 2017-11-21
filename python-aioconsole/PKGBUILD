_pkgname=aioconsole
pkgname=python-aioconsole
pkgver=0.1.4
pkgrel=1
pkgdesc="Asynchronous console and interfaces for asyncio"
arch=('any')
url="https://github.com/vxgmichel/aioconsole"
license=('GPLv3')
depends=('python' 'python-setuptools')
source=('https://pypi.python.org/packages/fc/c1/b746f3122a6bf2faee9edc000d1e815ef4de6145b9ff8ad62d0db4286a60/aioconsole-0.1.4.tar.gz')
md5sums=('15cfc136811da96559332d0b19b2e933')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
