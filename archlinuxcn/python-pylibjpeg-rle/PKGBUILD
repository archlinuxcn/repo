# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=pylibjpeg-rle
pkgname=python-pylibjpeg-rle
pkgver=1.2.0
pkgrel=1
pkgdesc='Fast DICOM RLE plugin for pylibjpeg'
arch=('x86_64')
url='https://github.com/pydicom/pylibjpeg-rle'
license=(MIT)
depends=(
  python-numpy
)
makedepends=(
  python-pip
  python-wheel
  python-setuptools
  python-setuptools-rust
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/pydicom/pylibjpeg-rle/archive/refs/tags/v${pkgver}.tar.gz")
sha512sums=('f9ddc4479e3abcabe78b4aff082a96883b2c7fb5a6500b17d8a3e8ef15fd079378dbcb7a2107f866ddfec7dea2f4ea0ce1e11044c27a95b3b5db7c4f6fa5c696')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py bdist_wheel
}

package() {
  cd "${_pkgname}-${pkgver}"
  PIP_CONFIG_FILE=/dev/null pip install --isolated --root="${pkgdir}" --ignore-installed --no-deps dist/*.whl
  python -O -m compileall "${pkgdir}/usr/lib"
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
