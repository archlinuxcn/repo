# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=einops
pkgname=python-einops
pkgver=0.7.1
pkgrel=1
pkgdesc='Deep learning operations reinvented (for pytorch, tensorflow, jax and others)'
arch=('any')
url='https://github.com/arogozhnikov/einops'
license=('MIT')
depends=(
  python
)
makedepends=(
  python-build
  python-hatchling
  python-installer
  python-wheel
)

source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/arogozhnikov/einops/archive/refs/tags/v${pkgver}.tar.gz")
sha512sums=('12c3381c054da2972500bb4257543c12c39b4f2e4d385398cc89f71693626ca4ac33ad7ebd2f0911cfa8ff7e5702b7ce32a4bd87f4d15f2c83c44d3782e6ce9d')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
