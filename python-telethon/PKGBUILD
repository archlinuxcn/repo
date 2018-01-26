_pkgname=Telethon
pkgname=python-telethon
pkgver=0.16.2.3
pkgrel=1
pkgdesc="Full-featured Telegram client library for Python 3"
arch=('any')
url="https://github.com/LonamiWebs/Telethon"
license=('MIT')
depends=('python' 'python-pyaes' 'python-rsa' 'python-setuptools')
source=('https://pypi.python.org/packages/46/e0/1bc043ac1d0d93a3bf12efd7be2375cf0c4e6d5b0346715dbb5d1f32c720/Telethon-0.16.2.3.tar.gz')
md5sums=('ab9c90101e7690c2c6bf5c6c22c55b67')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
