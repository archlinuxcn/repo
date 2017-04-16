_pkgname=aiosocks
pkgname=python-aiosocks
pkgver=0.2.2
pkgrel=1
pkgdesc="SOCKS proxy client for asyncio and aiohttp"
arch=('any')
url="https://github.com/nibrag/aiosocks"
license=('Apache')
depends=('python' 'python-setuptools')
source=('https://pypi.python.org/packages/1a/63/d324b547037f1b7438d1459b23bee19b77b8ca4bee05551526badea1f69f/aiosocks-0.2.2.tar.gz')
md5sums=('f0ca3c09d9690f0e10ba4db6537fb800')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
