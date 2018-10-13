_pkgname=trio
pkgname=python-trio
pkgver=0.9.0
pkgrel=1
pkgdesc="An async/await-native I/O library for humans and snake people"
arch=('any')
url="https://github.com/python-trio/trio"
license=('MIT')
depends=('python' 'python-attrs' 'python-sortedcontainers' 'python-idna' 'python-async_generator' 'python-outcome' 'python-sniffio')
makedepends=('python-setuptools')
provides=('python-multio-provider')
source=('https://files.pythonhosted.org/packages/69/70/d6f23892b898292736febebf4ead13cd0eb4df970dbf3498c7745c682835/trio-0.9.0.tar.gz')
md5sums=('987ccf27ee88def5c10f6f0a4d9f044f')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
