# Maintainer: Felix Yan <felixonmars@gmail.com>

pkgname=python2-py-bcrypt
pkgver=0.4
pkgrel=2
pkgdesc="py-bcrypt is an implementation the OpenBSD Blowfish password hashing algorithm"
arch=('i686' 'x86_64')
url="https://code.google.com/p/py-bcrypt/"
license=('MIT')
depends=('python2')
makedepends=('python2-setuptools')
source=("https://py-bcrypt.googlecode.com/files/py-bcrypt-${pkgver}.tar.gz")
md5sums=('dd8b367d6b716a2ea2e72392525f4e36')

package() {
  cd py-bcrypt-${pkgver}
  python2 setup.py install -O1 --prefix=/usr --root="${pkgdir}"
  install -d "${pkgdir}/usr/share/licenses/$pkgname"
  install -m 644 "$srcdir/py-bcrypt-${pkgver}/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"
}
