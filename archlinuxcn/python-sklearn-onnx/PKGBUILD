# Maintainer: Hu Butui <hot123tea123@gmail.com>

_pkgname=sklearn-onnx
pkgname=python-sklearn-onnx
pkgver=1.12
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
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/onnx/sklearn-onnx/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('782216a8cab111e8db7b0bb63cc8b4077b4ae29e3df770cfd7a47b7a5c3d8bd5')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
