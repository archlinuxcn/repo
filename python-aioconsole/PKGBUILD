_pkgname=aioconsole
pkgname=python-aioconsole
pkgver=0.1.7
pkgrel=1
pkgdesc="Asynchronous console and interfaces for asyncio"
arch=('any')
url="https://github.com/vxgmichel/aioconsole"
license=('GPLv3')
depends=('python' 'python-setuptools')
source=('https://pypi.python.org/packages/f3/53/ac3e648b2a1a75447b120079096f9950d11fc9dc1017bd57d2a476965470/aioconsole-0.1.7.tar.gz')
md5sums=('30f9b9e3ade490cbd88811d38d0c17f4')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
