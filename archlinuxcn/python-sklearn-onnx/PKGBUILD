# Maintainer: Hu Butui <hot123tea123@gmail.com>

_pkgname=sklearn-onnx
pkgname=python-sklearn-onnx
pkgver=1.10.4
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
sha256sums=('4ba094b4ba7b9d0e20acf56d4cc4663f0b8c1301742482b473362ea3e5586c9f')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
