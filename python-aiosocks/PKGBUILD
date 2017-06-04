_pkgname=aiosocks
pkgname=python-aiosocks
pkgver=0.2.3
pkgrel=1
pkgdesc="SOCKS proxy client for asyncio and aiohttp"
arch=('any')
url="https://github.com/nibrag/aiosocks"
license=('Apache')
depends=('python' 'python-setuptools')
source=('https://pypi.python.org/packages/cf/21/7193dc5fb364c635f032c84b8af61b09fd2862d85c032ba815d353b7c05d/aiosocks-0.2.3.tar.gz')
md5sums=('4ce5bcf143971cce387f1705d15d7418')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
