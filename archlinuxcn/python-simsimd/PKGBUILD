# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=SimSIMD
pkgname=python-simsimd
pkgver=6.3.1
pkgrel=1
pkgdesc='A Fast Dot Products & Similarity Metrics for Python using SIMD'
arch=('x86_64')
url='https://github.com/ashvardanian/simsimd'
license=('Apache-2.0')
depends=(
  gcc-libs
  glibc
)
makedepends=(
  python-build
  python-installer
  python-setuptools
  python-wheel
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/ashvardanian/SimSIMD/archive/refs/tags/v${pkgver}.tar.gz")
sha512sums=('9c809c9a8f064615f32409798465add8fbe94b614dd2a5468106980a79058e4a3d25d5055a562014c3008477290db6c4a3324ff2c3c8ee3970a32d797d60d28b')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
}
# vim:set ts=2 sw=2 et:
