# Maintainer: Yvaniak <ewen at philippot dot biz>
# Contributor: Achmad Fathoni <fathno dot id at gmail dot com>
# Contributor: Yigit Sever <yigit at yigitsever dot com>

pkgname=python-types-requests
_name=${pkgname#python-}
pkgver=2.32.0.20240712
pkgrel=1
pkgdesc="Typing stubs for requests"
arch=('any')
url="https://pypi.org/project/types-requests/"
license=('Apache-2.0')
depends=('python')
makedepends=('python-setuptools')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz")
sha256sums=('90c079ff05e549f6bf50e02e910210b98b8ff1ebdd18e19c873cd237737c1358')

build() {
  cd "$_name-$pkgver"
  python setup.py build
}

package() {
  cd "$_name-$pkgver"
  python setup.py install --root="$pkgdir" --optimize=1 --skip-build
}
