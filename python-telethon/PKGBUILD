_pkgname=Telethon
pkgname=python-telethon
pkgver=0.15.4.2
pkgrel=1
pkgdesc="Full-featured Telegram client library for Python 3"
arch=('any')
url="https://github.com/LonamiWebs/Telethon"
license=('MIT')
depends=('python' 'python-pyaes' 'python-rsa' 'python-setuptools')
source=('https://pypi.python.org/packages/56/a4/baedfa61c56a013b41f3c5580c109c23d83435d6a5283a9fe41cf8183feb/Telethon-0.15.4.2.tar.gz')
md5sums=('9042e7b80c3bc8120e5fea42f6371619')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
