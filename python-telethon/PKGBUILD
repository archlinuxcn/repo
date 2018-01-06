_pkgname=Telethon
pkgname=python-telethon
pkgver=0.16.0.7
pkgrel=1
pkgdesc="Full-featured Telegram client library for Python 3"
arch=('any')
url="https://github.com/LonamiWebs/Telethon"
license=('MIT')
depends=('python' 'python-pyaes' 'python-rsa' 'python-setuptools')
source=('https://pypi.python.org/packages/c2/7d/5554737d4bdbfa4e9658c25ea37fca23c2cc5fd18291effdc5556ec346a6/Telethon-0.16.0.7.tar.gz')
md5sums=('c3f4053ee83a9ccc190616ceb1a68a7d')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
