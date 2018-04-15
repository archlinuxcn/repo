_pkgname=Telethon
pkgname=python-telethon
pkgver=0.18.3
pkgrel=1
pkgdesc="Full-featured Telegram client library for Python 3"
arch=('any')
url="https://github.com/LonamiWebs/Telethon"
license=('MIT')
depends=('python' 'python-pyaes' 'python-rsa' 'python-setuptools')
source=('https://pypi.python.org/packages/8f/c3/cdc01fc22b2691d4abdd6c064baeb22ffd81dfe01ac7f518d652b8d22a32/Telethon-0.18.3.tar.gz')
md5sums=('118e5e3ee9072c1c5f185a26fe98b7bb')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
