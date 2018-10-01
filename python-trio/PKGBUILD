_pkgname=trio
pkgname=python-trio
pkgver=0.8.0
pkgrel=1
pkgdesc="An async/await-native I/O library for humans and snake people"
arch=('any')
url="https://github.com/python-trio/trio"
license=('MIT')
depends=('python' 'python-attrs' 'python-sortedcontainers' 'python-idna' 'python-async_generator' 'python-outcome' 'python-sniffio')
makedepends=('python-setuptools')
provides=('python-multio-provider')
source=('https://files.pythonhosted.org/packages/e1/cb/ddabcabc9ffaa45f89535267f33a22780045c6f9c02dcd725cc7a2b01496/trio-0.8.0.tar.gz')
md5sums=('77d91f7cd5476fbac85f851bd84981a8')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
