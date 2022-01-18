# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=einops
pkgname=python-einops
pkgver=0.4.0
pkgrel=1
pkgdesc='Deep learning operations reinvented (for pytorch, tensorflow, jax and others)'
arch=('any')
url='https://github.com/arogozhnikov/einops'
license=('MIT')
depends=(
  python
)
makedepends=(
  python-setuptools
)

source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/arogozhnikov/einops/archive/refs/tags/v${pkgver}.tar.gz")
sha512sums=('df02d756ac3c8f571e958f0303d4a9b006658642c03dca6b316d27436f60c18373f9ee5252bccf65c93187496f76f8ec6d17ace5cca682357efe34a37f460cec')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
