# Maintainer: Zhuoyun Wei <wzyboy@wzyboy.org>
# Contributor: "Amhairghin" Oscar Garcia Amor (https://ogarcia.me)

_pkgname='python-magic'
pkgname=python-magic-ahupp
pkgdesc='A python wrapper for libmagic'
pkgver=0.4.15
pkgrel=2
arch=('any')
url="https://github.com/ahupp/python-magic"
license=('MIT')
makedepends=('python-setuptools')
conflicts=('python-magic')
provides=('python-magic')
source=("https://github.com/ahupp/${_pkgname}/archive/${pkgver}.tar.gz")
sha256sums=('6d730389249ab1e34ffb0a3c5beaa44e116687ffa081e0176dab6c59ff271593')

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize='1'

  # doc file
  install -D -m644 README.md "${pkgdir}/usr/share/doc/${pkgname}/README.md"
}
