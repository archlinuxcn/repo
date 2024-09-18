# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=albucore
pkgname=python-albucore
pkgver=0.0.16
pkgrel=1
pkgdesc='A high-performance image processing library designed to optimize and extend the Albumentations library with specialized functions for advanced image transformations'
arch=('any')
url='https://github.com/albumentations-team/albucore'
license=('MIT')
depends=(
  python-numpy
  python-opencv
)
makedepends=(
  python-build
  python-installer
  python-setuptools
  python-wheel
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/albumentations-team/albucore/archive/refs/tags/${pkgver}.tar.gz")
sha512sums=('ae3637d454a336b8fbaefb3d06cc569a16456fde99c5110b9a472999294df07fae6921430a0bd708b2374d5e8f1caeac2f5c2ff231317d2ee3e89b4a4ad7c193')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
}
# vim:set ts=2 sw=2 et:
