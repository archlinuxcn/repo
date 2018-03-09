_pkgname=Telethon
pkgname=python-telethon
pkgver=0.18.0.2
pkgrel=1
pkgdesc="Full-featured Telegram client library for Python 3"
arch=('any')
url="https://github.com/LonamiWebs/Telethon"
license=('MIT')
depends=('python' 'python-pyaes' 'python-rsa' 'python-setuptools')
source=('https://pypi.python.org/packages/ca/3d/48038515ae233890e3476abe5f0bc218cfa63e2bc2f65e603204b6330aa0/Telethon-0.18.0.2.tar.gz')
md5sums=('39729f14b7f0ea928e5e77d504abd720')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
