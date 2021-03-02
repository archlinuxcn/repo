# Maintainer: Michael Riegert <michael at eowyn net>
# Contributor: Felix Golatofski <contact@xdfr.de>
# Contributor: Sibren Vasse <arch@sibrenvasse.nl>
# Contributor: Daniel M. Capella <polyzen@archlinux.info>
# Contributor: Morten Linderud <morten@linderud.pw>

pkgname=python-pychromecast
_name=${pkgname#python-}
pkgver=9.1.1
pkgrel=1
pkgdesc='Library for Python 3 to communicate with the Google Chromecast'
arch=('any')
url="https://github.com/home-assistant-libs/pychromecast"
license=('MIT')
depends=('python' 'python-protobuf' 'python-requests' 'python-zeroconf' 'python-six' 'python-setuptools' 'python-casttube')
makedepends=('python-setuptools')
source=("${pkgname}"-"${pkgver}".tar.gz::${url}/archive/$pkgver.tar.gz)
sha512sums=('7a4ceec47f8d8b183626329b5669b9366a8784e6e8867e21fa680ef87be8a6895345c4c76d3e8f90db2285e51d22465585caa8fd41ccb1109be248b72b9e1e2f')
conflicts=('python-pychromecast6')

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
