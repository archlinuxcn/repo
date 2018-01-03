_pkgname=aioconsole
pkgname=python-aioconsole
pkgver=0.1.6
pkgrel=1
pkgdesc="Asynchronous console and interfaces for asyncio"
arch=('any')
url="https://github.com/vxgmichel/aioconsole"
license=('GPLv3')
depends=('python' 'python-setuptools')
source=('https://pypi.python.org/packages/39/c5/7c85e13a7f20d5e662eb8faac4ae7db0ca1ddfd46f0a8609aa49d3584bec/aioconsole-0.1.6.tar.gz')
md5sums=('09673ec446ed22f58a21f6091c08c83c')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
