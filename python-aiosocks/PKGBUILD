_pkgname=aiosocks
pkgname=python-aiosocks
pkgver=0.2.5
pkgrel=1
pkgdesc="SOCKS proxy client for asyncio and aiohttp"
arch=('any')
url="https://github.com/nibrag/aiosocks"
license=('Apache')
depends=('python' 'python-setuptools')
source=('https://pypi.python.org/packages/4b/07/5778ee54ebc708e2104aec3d6cd212ed9842ba4695829dc44b6ccf1e630d/aiosocks-0.2.5.tar.gz')
md5sums=('04e2ff4ef4cbdd870eb3f84e32e99555')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
