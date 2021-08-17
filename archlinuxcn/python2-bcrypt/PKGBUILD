# Maintainer: Felix Yan <felixonmars@archlinux.org>
# Contributor: Lex Black <autumn-wind at web dot de>
# Contributor: Igor Nemilentsev <trezorg@gmail.com>
# Contributor: Alexander Diana <alexander@rouk.org>

pkgname=python2-bcrypt
pkgver=3.1.7
pkgrel=4
pkgdesc="Modern password hashing for your software and your servers"
arch=('x86_64')
url="https://github.com/pyca/bcrypt"
license=('Apache')
depends=('python2-cffi' 'python2-six')
makedepends=('python2-setuptools')
checkdepends=('python2-pytest')
source=("$pkgname-$pkgver.tar.gz::https://github.com/pyca/bcrypt/archive/$pkgver.tar.gz")
sha512sums=('bfe487ac43aa5081a16c7f67787c2aec777a9c42f3f0f64d4dd238e6cf135e248e806a675ecdc5240066e2b5a31773f9c5dd939479e96ec25357e27bced01409')

build() {
  cd bcrypt-$pkgver
  python2 setup.py build
}

check() {
  cd bcrypt-$pkgver
  PYTHONPATH="$PWD/build/lib.linux-$CARCH-2.7" pytest2
}

package() {
  cd bcrypt-$pkgver
  python2 setup.py install --prefix=/usr --root="$pkgdir"
}
