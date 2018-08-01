# Maintainer: Lari Tikkanen <lartza@wippies.com>

pkgname=python-pydle
_pkgname=pydle
pkgver=0.8.2
pkgrel=1
pkgdesc="A compact, flexible and standards-abiding IRC library for Python 3."
arch=(any)
url="https://github.com/Shizmob/pydle"
license=('BSD')
depends=('python' 'python-tornado')
makedepends=('python-setuptools')
source=("https://pypi.python.org/packages/source/p/pydle/pydle-$pkgver.tar.gz")
md5sums=('e5ecdcb64024cea1a69e4f0ab5cb4756')

build() {
  cd $_pkgname-$pkgver
  python setup.py build
}

package() {
  cd $_pkgname-$pkgver
  python setup.py install --root=$pkgdir --optimize=1
}
