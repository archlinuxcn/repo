# Maintainer: Hu Butui <hot123tea123@gmail.com>
# Contributor: Chih-Hsuan Yen <yan12125@archlinux.org>

_pkgname=onnxconverter-common
pkgname=python-onnxconverter-common
pkgver=1.8.1
pkgrel=2
pkgdesc='Common utilities for ONNX converters'
arch=('any')
url='https://github.com/microsoft/onnxconverter-common'
license=('MIT')
depends=(
  python-numpy
  python-onnx
  python-protobuf
)
makedepends=(
  python-setuptools
)
checkdepends=(
  python-onnxruntime
  python-pytest
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/microsoft/onnxconverter-common/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('f95f2a2d1fedc20cccbc820d4f63cbe84e287a5bd8c863ced400ae73946e13e6')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

check() {
  cd "${_pkgname}-${pkgver}"
  PYTHONPATH="${PWD}" pytest -v
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
