_pkgname=Telethon
pkgname=python-telethon
pkgver=0.18.2.3
pkgrel=1
pkgdesc="Full-featured Telegram client library for Python 3"
arch=('any')
url="https://github.com/LonamiWebs/Telethon"
license=('MIT')
depends=('python' 'python-pyaes' 'python-rsa' 'python-setuptools')
source=('https://pypi.python.org/packages/e0/5d/ba08769a32c02ba19dc41c493e22c8461c8fe6f608928ed62ef0788751da/Telethon-0.18.2.3.tar.gz')
md5sums=('abe51ee077159d287d1486142f12faae')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
