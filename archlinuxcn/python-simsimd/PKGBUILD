# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=SimSIMD
pkgname=python-simsimd
pkgver=6.4.2
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
sha512sums=('889b5b9c566849c8139bb3867abc60045c17c05ce96bf2d0832d065d84489d9a2a05f778b56b5cc45604c510b82b534f840fcc38222bac3d237c607aa4a51711')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
}
# vim:set ts=2 sw=2 et:
