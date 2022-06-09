# Maintainer: Zhuoyun Wei <wzyboy@wzyboy.org>
# Contributor: "Amhairghin" Oscar Garcia Amor (https://ogarcia.me)

_pkgname='python-magic'
pkgname=python-magic-ahupp
pkgdesc='A python wrapper for libmagic'
pkgver=0.4.27
pkgrel=1
arch=('any')
url="https://github.com/ahupp/python-magic"
license=('MIT')
depends=('python')
makedepends=('python-setuptools')
provides=('python-magic')
source=("https://github.com/ahupp/${_pkgname}/archive/${pkgver}.tar.gz")
sha256sums=('3978a25d43d9a7b8a89ae9d726bd4962fc90dc4f69ae852e399f3c56d4b0bd63')

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize='1'

  install -D -m644 README.md "${pkgdir}/usr/share/doc/${pkgname}/README.md"
  install -D -m644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
