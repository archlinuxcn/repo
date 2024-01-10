# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=pylibjpeg-rle
pkgname=python-pylibjpeg-rle
pkgver=2.0.0
pkgrel=1
pkgdesc='Fast DICOM RLE plugin for pylibjpeg'
arch=('x86_64')
url='https://github.com/pydicom/pylibjpeg-rle'
license=(MIT)
depends=(
  python-numpy
)
makedepends=(
  python-build
  python-installer
  python-maturin
  python-wheel
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/pydicom/pylibjpeg-rle/archive/refs/tags/v${pkgver}.tar.gz")
sha512sums=('8776be5f4b4cdfc6f40217486361b07ab9626ff488210e63619f4b26f6ca8270733c09f27cccce16879306b908721d5d1a9d506b666fd0908351faeba2b38ca9')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
}
# vim:set ts=2 sw=2 et:
