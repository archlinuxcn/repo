# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=yacs
pkgname=python-yacs
pkgver=0.1.7
pkgrel=1
pkgdesc='Yet Another Configuration System'
arch=('any')
url='https://github.com/rbgirshick/yacs'
license=('BSD')
makedepends=(
  python-setuptools
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/rbgirshick/yacs/archive/v${pkgver}.tar.gz")
sha512sums=('aa00e6eedbdbffbb11d9302ea723ed010e22920dc73e466fe403cfd65c8ede80f95153cf0fd8ef06bedb392c741c259aeae7b87bd9b95df5e4d0d1d0ac2d4486')

build() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 "LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
