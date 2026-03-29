# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=NumKong
pkgname=python-numkong
pkgver=7.2.4
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
sha512sums=('1585f055a4f0bc1f86b07a5f3af21970cceb4f7b2b41d50f3e1d0474fc52b198b7dda6168d289e51c2ab419d5407a99673e6b900db45f30776150752ff2f24f9')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
}
# vim:set ts=2 sw=2 et:
