_pkgname=Telethon
pkgname=python-telethon
pkgver=0.18
pkgrel=1
pkgdesc="Full-featured Telegram client library for Python 3"
arch=('any')
url="https://github.com/LonamiWebs/Telethon"
license=('MIT')
depends=('python' 'python-pyaes' 'python-rsa' 'python-setuptools')
source=('https://pypi.python.org/packages/7a/00/33b0aca6f5fbfc4b065e0708923f329157fc6adda8f0a4b08b853ee79461/Telethon-0.18.tar.gz')
md5sums=('d8d62b6f612e2d86312f814be5829a9f')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
