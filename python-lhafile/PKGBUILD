# Maintainer: grimi <grimi at poczta dot fm>

pkgname=python-lhafile
pkgver=0.2.1
pkgrel=1
pkgdesc="LHA archive support for Python 3"
arch=('i686' 'x86_64')
url="http://fengestad.no/python-lhafile/"
license=('BSD')
depends=('python')
source=("http://fengestad.no/${pkgname}/${pkgname}-${pkgver}.tar.gz")
md5sums=('bc63d61a1b562bbbc52118c168f8cb5e')


package() {
  cd ${pkgname}-${pkgver}
  python3 setup.py install --root="${pkgdir}/" --optimize=1
  install -Dm644 COPYING.txt "${pkgdir}"/usr/share/licenses/${pkgname}/COPYING
}

# vim:set ts=2 sw=2 et:
