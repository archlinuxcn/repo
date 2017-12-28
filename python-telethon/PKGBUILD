_pkgname=Telethon
pkgname=python-telethon
pkgver=0.16.0.3
pkgrel=1
pkgdesc="Full-featured Telegram client library for Python 3"
arch=('any')
url="https://github.com/LonamiWebs/Telethon"
license=('MIT')
depends=('python' 'python-pyaes' 'python-rsa' 'python-setuptools')
source=('https://pypi.python.org/packages/8c/2c/913284110ae13a8cdfe553157215e5e2fd9bb0564324b802cfa9f44a8c55/Telethon-0.16.0.3.tar.gz')
md5sums=('53e65c9aa48ef9780329aef1c153f0ef')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
