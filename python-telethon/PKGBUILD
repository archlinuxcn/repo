_pkgname=Telethon
pkgname=python-telethon
pkgver=0.17
pkgrel=1
pkgdesc="Full-featured Telegram client library for Python 3"
arch=('any')
url="https://github.com/LonamiWebs/Telethon"
license=('MIT')
depends=('python' 'python-pyaes' 'python-rsa' 'python-setuptools')
source=('https://pypi.python.org/packages/c6/9c/a5806811ab61f57af3cc318882e25b0a12e1d73a899c2b271cb3ff3b8ca5/Telethon-0.17.tar.gz')
md5sums=('edf950720323aeeb590d36acf1af6452')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
