# Maintainer: Sibren Vasse <arch@sibrenvasse.nl>
# Contributor: Daniel M. Capella <polyzen@archlinux.info>
# Contributor: Morten Linderud <morten@linderud.pw>

pkgname=python-pychromecast
_name=${pkgname#python-}
pkgver=6.0.0
pkgrel=1
pkgdesc='Library for Python 3 to communicate with the Google Chromecast'
arch=('any')
url=https://github.com/balloob/pychromecast
license=('MIT')
depends=('python' 'python-protobuf' 'python-requests' 'python-zeroconf' 'python-six' 'python-setuptools' 'python-casttube')
makedepends=('python-setuptools')
source=("https://github.com/balloob/pychromecast/archive/$pkgver.tar.gz")
sha512sums=('7fdddcd2bdc332ae167cb50bf9b33c85ee6d93b7d2a76908761e1a371d1210fe86554cfd204f9ad2ad162f2b29e088d8eaa7584a7ab7f92b682c242a31d7495c')

build() {
  cd "$_name-$pkgver"
  python setup.py build
}

package() {
  cd "$_name-$pkgver"
  python setup.py install --root="$pkgdir" --optimize=1 --skip-build
  install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

# vim:set ts=2 sw=2 et:
