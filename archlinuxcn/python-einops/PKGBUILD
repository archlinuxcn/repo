# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=einops
pkgname=python-einops
pkgver=0.6.0
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
sha512sums=('4ae3bfee5a77481e30b661772c53f463a9f84f18da140f90466ccd527c4b4f8be83fde4112df90e6a087ab4bbc835c954974c85b06254ae383bfad60f700996f')

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
