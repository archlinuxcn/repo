# Maintainer: Zhuoyun Wei <wzyboy@wzyboy.org>
# Contributor: "Amhairghin" Oscar Garcia Amor (https://ogarcia.me)

_pkgname='python-magic'
pkgname=python-magic-ahupp
pkgdesc='A python wrapper for libmagic'
pkgver=0.4.22
pkgrel=2
arch=('any')
url="https://github.com/ahupp/python-magic"
license=('MIT')
depends=('python')
makedepends=('python-setuptools')
provides=('python-magic')
source=("https://github.com/ahupp/${_pkgname}/archive/${pkgver}.tar.gz")
sha256sums=('cd4be7884304720a59e72a32e578c0fe676e4cdd2664778ba105469b4c201189')

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize='1'

  install -D -m644 README.md "${pkgdir}/usr/share/doc/${pkgname}/README.md"
  install -D -m644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
