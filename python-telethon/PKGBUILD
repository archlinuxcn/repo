_pkgname=Telethon
pkgname=python-telethon
pkgver=0.16.1.1
pkgrel=1
pkgdesc="Full-featured Telegram client library for Python 3"
arch=('any')
url="https://github.com/LonamiWebs/Telethon"
license=('MIT')
depends=('python' 'python-pyaes' 'python-rsa' 'python-setuptools')
source=('https://pypi.python.org/packages/54/5d/46e0170ff4feec22bfa35ded2013696d34f101f82ddb7eb7af95c517cd9a/Telethon-0.16.1.1.tar.gz')
md5sums=('38ac2af824edca983c551ccdf5d9309b')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
