_pkgname=Telethon
pkgname=python-telethon
pkgver=0.16.0.4
pkgrel=1
pkgdesc="Full-featured Telegram client library for Python 3"
arch=('any')
url="https://github.com/LonamiWebs/Telethon"
license=('MIT')
depends=('python' 'python-pyaes' 'python-rsa' 'python-setuptools')
source=('https://pypi.python.org/packages/bd/fa/fa4569bb82426f2f29bc160cc37a8c5b31a0312a97b7ab4f0850183d4da1/Telethon-0.16.0.4.tar.gz')
md5sums=('301a1f86290c33d268fa4a1ef6dc38b5')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
