_pkgname=aiosocks
pkgname=python-aiosocks
pkgver=0.2.6
pkgrel=1
pkgdesc="SOCKS proxy client for asyncio and aiohttp"
arch=('any')
url="https://github.com/nibrag/aiosocks"
license=('Apache')
depends=('python' 'python-setuptools')
source=('https://pypi.python.org/packages/c7/60/284a4909410906979ef44a9fa24421072f98b747d9916a3b98d50461abbe/aiosocks-0.2.6.tar.gz')
md5sums=('cbe53d1ff7c4537b66d5515d90ac1bc5')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
