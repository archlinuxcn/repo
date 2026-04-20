# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=NumKong
pkgname=python-numkong
pkgver=7.6.0
pkgrel=1
pkgdesc='A Fast Dot Products & Similarity Metrics for Python using SIMD'
arch=('x86_64')
url='https://github.com/ashvardanian/numkong'
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
provides=(
  python-simsimd
)
replaces=(
  python-simsimd
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/ashvardanian/SimSIMD/archive/refs/tags/v${pkgver}.tar.gz")
sha512sums=('0454cc0168d3cd3a3d176cdfc879bfa2b4752b036248f7a7445a22dd1bd0c1f1c78a68e50fd15c8d0f0c10d234de28cc3cea906c37d01850e8939aecddd86b91')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
}
# vim:set ts=2 sw=2 et:
