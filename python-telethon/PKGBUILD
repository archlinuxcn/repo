_pkgname=Telethon
pkgname=python-telethon
pkgver=0.15.5.2
pkgrel=1
pkgdesc="Full-featured Telegram client library for Python 3"
arch=('any')
url="https://github.com/LonamiWebs/Telethon"
license=('MIT')
depends=('python' 'python-pyaes' 'python-rsa' 'python-setuptools')
source=('https://pypi.python.org/packages/5c/48/389080ddc526cbf7f1077bd8ba9df2211e4745d4ec8379f9a4a5b31fce2b/Telethon-0.15.5.2.tar.gz')
md5sums=('74a7e418b9cf34435b0a7c3702f2a6ee')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
