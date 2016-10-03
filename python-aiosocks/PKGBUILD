_pkgname=aiosocks
pkgname=python-aiosocks
pkgver=0.1.7
pkgrel=1
pkgdesc="SOCKS proxy client for asyncio and aiohttp"
arch=('any')
url="https://github.com/nibrag/aiosocks"
license=('Apache')
depends=('python' 'python-setuptools')
source=('https://pypi.python.org/packages/cd/d5/f522e746a07b0e454dc1d909d1494d55f7da6bc0e4671e27175691046a95/aiosocks-0.1.7.zip')
md5sums=('46b2c6564e8af97ce6a8ad66fe632de3')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"

  python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
