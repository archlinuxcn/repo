_pkgname=aiosocks
pkgname=python-aiosocks
pkgver=0.2.4
pkgrel=1
pkgdesc="SOCKS proxy client for asyncio and aiohttp"
arch=('any')
url="https://github.com/nibrag/aiosocks"
license=('Apache')
depends=('python' 'python-setuptools')
source=('https://pypi.python.org/packages/2e/2d/c59f47a339c86f6e42b9ce9d0a718488003ec3662f48b9e505128385137a/aiosocks-0.2.4.tar.gz')
md5sums=('f12e7a8abd5a5452ed510df108f4d1c8')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
