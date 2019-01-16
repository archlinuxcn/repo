_pkgname=outcome
pkgname=python-outcome
pkgver=1.0.0
pkgrel=2
pkgdesc="Capture the outcome of Python function calls."
arch=('any')
url="https://github.com/python-trio/outcome"
license=('MIT')
depends=('python' 'python-attrs')
_name=${pkgname#python-}
makedepends=('python-setuptools')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.tar.gz")
md5sums=('61a71fc9d70bbb3ebaff51db6bfcd27d')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
