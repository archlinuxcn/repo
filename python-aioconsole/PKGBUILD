_pkgname=aioconsole
pkgname=python-aioconsole
pkgver=0.1.3
pkgrel=1
pkgdesc="Asynchronous console and interfaces for asyncio"
arch=('any')
url="https://github.com/vxgmichel/aioconsole"
license=('GPLv3')
depends=('python')
source=('https://pypi.python.org/packages/87/2d/0587d3ee28519dcd37a5bbf172043463a49884d69fe229f46e6d537767c2/aioconsole-0.1.3.tar.gz')
md5sums=('1c9b24847e48ffd32921be69d3ea0f0a')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
