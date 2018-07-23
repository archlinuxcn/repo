_pkgname=aioconsole
pkgname=python-aioconsole
pkgver=0.1.10
pkgrel=1
pkgdesc="Asynchronous console and interfaces for asyncio"
arch=('any')
url="https://github.com/vxgmichel/aioconsole"
license=('GPLv3')
depends=('python' 'python-setuptools')
source=('https://files.pythonhosted.org/packages/c0/a2/e67a62f735d60a8e433db212446c1010861d44ff0080fb758a604b79dde7/aioconsole-0.1.10.tar.gz')
md5sums=('cc383663a6b132bafbdcc21fb5c56ec3')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
