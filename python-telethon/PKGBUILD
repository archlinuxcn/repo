_pkgname=Telethon
pkgname=python-telethon
pkgver=0.16.0.11
pkgrel=1
pkgdesc="Full-featured Telegram client library for Python 3"
arch=('any')
url="https://github.com/LonamiWebs/Telethon"
license=('MIT')
depends=('python' 'python-pyaes' 'python-rsa' 'python-setuptools')
source=('https://pypi.python.org/packages/cf/48/7c3fd015d4cfe405fe9e4d7b1fac918eda1c6a74f49813b0372ac99e7aed/Telethon-0.16.0.11.tar.gz')
md5sums=('66c56f5708ecd7326f2a185d2a42a9a2')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
