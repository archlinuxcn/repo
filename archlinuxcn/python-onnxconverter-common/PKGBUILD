# Maintainer: Hu Butui <hot123tea123@gmail.com>
# Contributor: Chih-Hsuan Yen <yan12125@archlinux.org>

_pkgname=onnxconverter-common
pkgname=python-onnxconverter-common
pkgver=1.15.0
pkgrel=1
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
sha256sums=('21588945e9b844826e8326e17ed646f3dd2c2c387fe722b5138559c2567146bf')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
