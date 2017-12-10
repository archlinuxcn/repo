_pkgname=aioconsole
pkgname=python-aioconsole
pkgver=0.1.5
pkgrel=1
pkgdesc="Asynchronous console and interfaces for asyncio"
arch=('any')
url="https://github.com/vxgmichel/aioconsole"
license=('GPLv3')
depends=('python' 'python-setuptools')
source=('https://pypi.python.org/packages/a3/c4/756c698695238685919ae31a5e728e229a171fa90ab38be22df28ccfe9c0/aioconsole-0.1.5.tar.gz')
md5sums=('620bb8708d2c8726a38c2d416d6c6f74')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
