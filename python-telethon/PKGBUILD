_pkgname=Telethon
pkgname=python-telethon
pkgver=1.0.4
pkgrel=1
pkgdesc="Full-featured Telegram client library for Python 3"
arch=('any')
url="https://github.com/LonamiWebs/Telethon"
license=('MIT')
depends=('python' 'python-pyaes' 'python-rsa' 'python-setuptools')
source=('https://files.pythonhosted.org/packages/82/e1/69a66509678960037f95c7ab237f6fcfd58b797206bd8a71d80eaf1fb8f4/Telethon-1.0.4.tar.gz')
md5sums=('ec6fda8f21c469f3ecd9d8a575049306')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
