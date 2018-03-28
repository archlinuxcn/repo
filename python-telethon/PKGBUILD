_pkgname=Telethon
pkgname=python-telethon
pkgver=0.18.2.1
pkgrel=1
pkgdesc="Full-featured Telegram client library for Python 3"
arch=('any')
url="https://github.com/LonamiWebs/Telethon"
license=('MIT')
depends=('python' 'python-pyaes' 'python-rsa' 'python-setuptools')
source=('https://pypi.python.org/packages/d9/d8/e00adab081b4d0b4f25669a236b489cec5881cd072ed84f35c49c2d0fc5f/Telethon-0.18.2.1.tar.gz')
md5sums=('a697a75b3348d089dd65fc0a19b29685')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
