# Maintainer: Felix Yan <felixonmars@archlinux.org>

pkgname=python2-phonenumbers
_pkgname=phonenumbers
pkgver=7.0.2
pkgrel=1
pkgdesc="Python version of Google's common library for parsing, formatting, storing and validating international phone numbers"
arch=('any')
url="https://github.com/daviddrysdale/python-phonenumbers"
license=('APACHE')
makedepends=("python2-setuptools")
depends=('python2')
source=("https://pypi.python.org/packages/source/p/$_pkgname/$_pkgname-$pkgver.tar.gz")
sha512sums=('036bf99c98a787ec64bc0fd63913fb59276bab344f2a5d7b3712040388b530aaeadbd1ebc6b6395b19b18123b9e9f66d5ad806ad0f4ffeccbd0504be3cd0b33e')

package() {
  cd $_pkgname-$pkgver
  python2 setup.py install -O1 --root "${pkgdir}"
}
