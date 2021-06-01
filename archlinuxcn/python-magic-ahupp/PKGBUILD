# Maintainer: Zhuoyun Wei <wzyboy@wzyboy.org>
# Contributor: "Amhairghin" Oscar Garcia Amor (https://ogarcia.me)

_pkgname='python-magic'
pkgname=python-magic-ahupp
pkgdesc='A python wrapper for libmagic'
pkgver=0.4.23
pkgrel=1
arch=('any')
url="https://github.com/ahupp/python-magic"
license=('MIT')
depends=('python')
makedepends=('python-setuptools')
provides=('python-magic')
source=("https://github.com/ahupp/${_pkgname}/archive/${pkgver}.tar.gz")
sha256sums=('616de44fd9a9e9b5a2bd82913cb912291c224f4434119ff6a564235ea9401db9')

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize='1'

  install -D -m644 README.md "${pkgdir}/usr/share/doc/${pkgname}/README.md"
  install -D -m644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
