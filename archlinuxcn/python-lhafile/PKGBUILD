# Maintainer: grimi

pkgname=python-lhafile
pkgver=0.2.2
pkgrel=1
pkgdesc="LHA archive support for Python 3"
arch=('i686' 'x86_64')
url="http://fengestad.no/python-lhafile/"
license=('BSD')
depends=('python')
#source=("http://fengestad.no/${pkgname}/${pkgname}-${pkgver}.tar.gz")
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/FrodeSolheim/${pkgname}/archive/v${pkgver}.tar.gz")
sha256sums=('18396276b77d8c7e094f169d3b2471e60de3d412a2454a0f73c452a54817ee68')


prepare() {
  cd ${pkgname}-${pkgver}
  sed "s/version='0.2.1'/version='0.2.2'/" -i setup.py
}

package() {
  cd ${pkgname}-${pkgver}
  python3 setup.py install --root="${pkgdir}/" --optimize=1
  install -Dm644 COPYING.txt "${pkgdir}"/usr/share/licenses/${pkgname}/COPYING
}

# vim:set ts=2 sw=2 et:
