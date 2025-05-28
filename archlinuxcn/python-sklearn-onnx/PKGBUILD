# Maintainer: Hu Butui <hot123tea123@gmail.com>

_pkgname=sklearn-onnx
pkgname=python-sklearn-onnx
pkgver=1.19.1
pkgrel=1
pkgdesc='Convert scikit-learn models and pipelines to ONNX'
arch=('any')
url='https://github.com/onnx/sklearn-onnx'
license=('Apache-2.0')
depends=(
  python-numpy
  python-scipy
  python-onnx
  python-protobuf
  python-scikit-learn
  python-onnxconverter-common
)
makedepends=(
  python-build
  python-installer
  python-setuptools
  python-wheel
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/onnx/sklearn-onnx/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('9487611004ccd9510cd657fa3b7dc1dff299a202dd977efcd3c616c87aeae338')

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

