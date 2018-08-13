_pkgname=trio
pkgname=python-trio
pkgver=0.6.0
pkgrel=1
pkgdesc="An async/await-native I/O library for humans and snake people"
arch=('any')
url="https://github.com/python-trio/trio"
license=('MIT')
depends=('python' 'python-attrs' 'python-sortedcontainers' 'python-idna' 'python-async_generator')
makedepends=('python-setuptools')
provides=('python-multio-provider')
source=('https://files.pythonhosted.org/packages/19/fe/4e3b7aa398392433e989df7aa9f1ffdeec978588b499cfb29e2e3546121e/trio-0.6.0.tar.gz')
md5sums=('a4d0e675c777ab01ea822470660e3e3d')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
