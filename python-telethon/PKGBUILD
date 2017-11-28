_pkgname=Telethon
pkgname=python-telethon
pkgver=0.15.5.7
pkgrel=1
pkgdesc="Full-featured Telegram client library for Python 3"
arch=('any')
url="https://github.com/LonamiWebs/Telethon"
license=('MIT')
depends=('python' 'python-pyaes' 'python-rsa' 'python-setuptools')
source=('https://pypi.python.org/packages/94/bd/c0f12dc07b29d9d88ab884cb38afe8d78f3588878c2df95eaf37705989ab/Telethon-0.15.5.7.tar.gz')
md5sums=('d714e2848c9ea1e61fcce31b03a6ab45')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
