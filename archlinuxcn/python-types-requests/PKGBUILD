# Maintainer: Yvaniak <ewen at philippot dot biz>
# Contributor: Achmad Fathoni <fathno dot id at gmail dot com>
# Contributor: Yigit Sever <yigit at yigitsever dot com>

pkgname=python-types-requests
_name=${pkgname#python-}
pkgver=2.32.0.20241016
pkgrel=1
pkgdesc="Typing stubs for requests"
arch=('any')
url="https://pypi.org/project/types-requests/"
license=('Apache-2.0')
depends=('python')
makedepends=('python-setuptools')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz")
sha256sums=('0d9cad2f27515d0e3e3da7134a1b6f28fb97129d86b867f24d9c726452634d95')

build() {
  cd "$_name-$pkgver"
  python setup.py build
}

package() {
  cd "$_name-$pkgver"
  python setup.py install --root="$pkgdir" --optimize=1 --skip-build
}
