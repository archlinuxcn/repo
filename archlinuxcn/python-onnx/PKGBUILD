# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-onnx
pkgver=12.0.0
pkgrel=1
pkgdesc='Open Neural Network Exchange'
arch=('x86_64')
url='https://onnx.ai'
license=('MIT')
depends=(
  protobuf
  python-protobuf
  python-numpy
  python-six
  python-typing_extensions
)
makedepends=(
  cmake
  git
  python-setuptools
  python-pip
)
source=("${pkgname}::git+https://github.com/onnx/onnx.git#tag=v${pkgver}")
sha512sums=('SKIP')

prepare() {
  cd "${pkgname}"
  git submodule update --init --recursive
  # Partial backpart from https://github.com/onnx/onnx/pull/3674
  sed -i 's#collections.Iterable#collections.abc.Iterable#g' onnx/helper.py
}

build() {
  cd "${pkgname}"
  python setup.py build
}

package() {
  cd "${pkgname}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
