_pkgname=Telethon
pkgname=python-telethon
pkgver=0.16.1
pkgrel=1
pkgdesc="Full-featured Telegram client library for Python 3"
arch=('any')
url="https://github.com/LonamiWebs/Telethon"
license=('MIT')
depends=('python' 'python-pyaes' 'python-rsa' 'python-setuptools')
source=('https://pypi.python.org/packages/c0/31/26fd059decd81a13f9217352d648d30a46e5a20632d1afe90e57f9b08157/Telethon-0.16.1.tar.gz')
md5sums=('4ed81ec8914aa9df6387a6b8618da3ac')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
