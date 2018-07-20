_pkgname=trio
pkgname=python-trio
pkgver=0.5.0
pkgrel=1
pkgdesc="An async/await-native I/O library for humans and snake people"
arch=('any')
url="https://github.com/python-trio/trio"
license=('MIT')
depends=('python' 'python-attrs' 'python-sortedcontainers' 'python-idna' 'python-async_generator')
makedepends=('python-setuptools')
provides=('python-multio-provider')
source=('https://files.pythonhosted.org/packages/37/75/1d0c6f3ab220c54dfde2c2c0b3547f6d275389e18c14aa74dcf86985549b/trio-0.5.0.tar.gz')
md5sums=('ec533fdd8865761d1bc2e43a8ca9521f')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
