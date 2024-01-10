# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=PhiK
pkgname=python-phik
pkgver=0.12.4
pkgrel=1
pkgdesc='Phi_K correlation analyzer library'
arch=('x86_64')
url='https://github.com/kaveio/phik'
license=('Apache')
depends=(
  python-joblib
  python-matplotlib
  python-numpy
  python-pandas
  python-scipy
)
makedepends=(
  cmake
  pybind11
  python-build
  python-installer
  python-scikit-build-core
  python-wheel
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/KaveIO/PhiK/archive/refs/tags/v${pkgver}.tar.gz")
sha512sums=('eff5c36395003ee7a6832654cd57968e4a4f65170ef7a4abf629a67e5ef918efd231fda9aa4cd4234c1bb0b83fc7481accf2f0dd85af73b6f9a5d115324bb844')

build() {
  cd "${_pkgname}-${pkgver}"
  CMAKE_GENERATOR="Unix Makefiles" \
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="$pkgdir" dist/*.whl
}
# vim:set ts=2 sw=2 et:
