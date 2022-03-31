# Maintainer: Hu Butui <hot123tea123@gmail.com>

_pkgname=sklearn-onnx
pkgname=python-sklearn-onnx
pkgver=1.11.1
pkgrel=1
pkgdesc='Convert scikit-learn models and pipelines to ONNX'
arch=('any')
url='https://github.com/onnx/sklearn-onnx'
license=('Apache')
depends=(
  python-numpy
  python-scipy
  python-onnx
  python-protobuf
  python-scikit-learn
  python-onnxconverter-common
)
makedepends=(
  python-setuptools
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/onnx/sklearn-onnx/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('0b45e70d3e29e2c22c8586803392b40f3eb979439c3ac7249d0c61ff09801a98')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
