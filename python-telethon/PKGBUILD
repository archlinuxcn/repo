_pkgname=Telethon
pkgname=python-telethon
pkgver=0.15.5.5
pkgrel=1
pkgdesc="Full-featured Telegram client library for Python 3"
arch=('any')
url="https://github.com/LonamiWebs/Telethon"
license=('MIT')
depends=('python' 'python-pyaes' 'python-rsa' 'python-setuptools')
source=('https://pypi.python.org/packages/2f/df/5918786dfe8e82fe0e3bc37a6abe6c6c3e361b843e0d8788f1f0e4f66c72/Telethon-0.15.5.5.tar.gz')
md5sums=('0a754fb80c894425b77b893f194ec018')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
