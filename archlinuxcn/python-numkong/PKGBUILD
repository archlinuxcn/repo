# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=NumKong
pkgname=python-numkong
pkgver=7.4.4
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
sha512sums=('5af620701996ea1ca7df4bcada0303d4560d0f50e5a48489c30990a3991a67f2a66f7a7683ac1b5c5d7f5153864b0349b9e85c117402ec4a9b72442021f917fe')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
}
# vim:set ts=2 sw=2 et:
