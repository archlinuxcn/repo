_pkgname=Telethon
pkgname=python-telethon
pkgver=0.15.4
pkgrel=1
pkgdesc="Full-featured Telegram client library for Python 3"
arch=('any')
url="https://github.com/LonamiWebs/Telethon"
license=('MIT')
depends=('python' 'python-pyaes' 'python-rsa' 'python-setuptools')
source=('https://pypi.python.org/packages/ef/62/adbdd2cabf4595ff7af94dc5e8d6dc96fb2a43fa80ec4f7cc919d51067a7/Telethon-0.15.4.tar.gz')
md5sums=('2238f5b47e6420a3a37b3806b97cebe7')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
