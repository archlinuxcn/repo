_pkgname=trio
pkgname=python-trio
pkgver=0.10.0
pkgrel=1
pkgdesc="An async/await-native I/O library for humans and snake people"
arch=('any')
url="https://github.com/python-trio/trio"
license=('MIT')
depends=('python' 'python-attrs' 'python-sortedcontainers' 'python-idna' 'python-async_generator' 'python-outcome' 'python-sniffio')
_name=${pkgname#python-}
makedepends=('python-setuptools')
provides=('python-multio-provider')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.tar.gz")
md5sums=('b79227f6eabbeccd0703f8e42801bd1e')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
