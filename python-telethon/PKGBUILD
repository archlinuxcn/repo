_pkgname=Telethon
pkgname=python-telethon
pkgver=1.0.3
pkgrel=1
pkgdesc="Full-featured Telegram client library for Python 3"
arch=('any')
url="https://github.com/LonamiWebs/Telethon"
license=('MIT')
depends=('python' 'python-pyaes' 'python-rsa' 'python-setuptools')
source=('https://files.pythonhosted.org/packages/6f/97/d6b4ca6fdbf3050cbedcb111714c377eeb86ea18775c4804204ea7f4a5ca/Telethon-1.0.3.tar.gz')
md5sums=('48682066a415ea695306a2a6976a6cf0')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
