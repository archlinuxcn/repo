# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=pylibjpeg-rle
pkgname=python-pylibjpeg-rle
pkgver=2.2.0
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
sha512sums=('151c10460d1f9be6f3d67d897f5c030f48b6f85acca78b351b78465cb881eddc57bf302e13855d708e3202428ef9f12a72ec4234e6034e1b35e573c207413ad7')

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
