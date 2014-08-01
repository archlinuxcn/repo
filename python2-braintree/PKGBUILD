# Maintainer: Felix Yan <felixonmars@gmail.com>

pkgname=python2-braintree
_pkgname=braintree
pkgver=3.2.0
pkgrel=1
pkgdesc="Braintree Python Library"
arch=('any')
url="https://www.braintreepayments.com/docs/python"
license=('MIT')
makedepends=("python2-setuptools")
depends=('python2-requests')
source=("https://github.com/braintree/braintree_python/archive/${pkgver}.tar.gz")

package() {
  cd ${_pkgname}_python-$pkgver
  python2 setup.py install --root "${pkgdir}"

  install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

sha512sums=('0abef7f5375d5e64c526ddfc9216b7d934297641b6dc82ed735091d3bb31a83ee5ac27f16b9ed0b90ac48236afef7a7f314fffd6f28ef8f96ae5b9d7b79f8815')
