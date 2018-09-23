_pkgname=Telethon
pkgname=python-telethon
pkgver=1.3
pkgrel=1
pkgdesc="Full-featured Telegram client library for Python 3"
arch=('any')
url="https://github.com/LonamiWebs/Telethon"
license=('MIT')
depends=('python' 'python-pyaes' 'python-rsa' 'python-setuptools')
source=('https://files.pythonhosted.org/packages/86/b0/af48e7b0530bef9f88f7c8f4bd1f4f4b421f587268358191839cff792bf3/Telethon-1.3.tar.gz')
md5sums=('fe1e8f0c911f2beb681b28d44c2be23a')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
