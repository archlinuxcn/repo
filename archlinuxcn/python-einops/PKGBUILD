# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=einops
pkgname=python-einops
pkgver=0.6.1
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
sha512sums=('41910e1356912a716d0e3f9a40aec842407d3936ebdb46f4784dbec29050a0fc582c4dfc9deca0ddd77fa516929005858b580219d0993786bf2ffa2b677c81d1')

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
