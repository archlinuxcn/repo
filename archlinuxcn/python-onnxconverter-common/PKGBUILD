# Maintainer: Hu Butui <hot123tea123@gmail.com>
# Contributor: Chih-Hsuan Yen <yan12125@archlinux.org>

_pkgname=onnxconverter-common
pkgname=python-onnxconverter-common
pkgver=1.9.0
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
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/microsoft/onnxconverter-common/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('32315bcc844a8203092f3117a4a092ac6cf03d6a20145477e284f1172557d6f9')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
