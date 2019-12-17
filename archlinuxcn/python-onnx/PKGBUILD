# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-onnx
pkgver=1.6.0
pkgrel=8
pkgdesc='Open Neural Network Exchange'
arch=('x86_64')
url='https://onnx.ai'
license=('MIT')
depends=(
  'protobuf'
  'python-protobuf'
  'python-numpy'
  'python-six'
  'python-typing_extensions'
)
makedepends=(
  'cmake'
  'git'
  'python-setuptools'
)
checkdepends=(
  'python-nbval' 
  'python-nose' 
  'python-pytest' 
  'python-scipy'
  ${optdepends[@]}
)
optdepends=(
  'mxnet'
  'python-pytorch'
  'python-tensorflow'
)
source=("${pkgname}::git+https://github.com/onnx/onnx.git#tag=v${pkgver}")
sha512sums=('SKIP')

get_pyver() {
  python -c 'import sys; print(str(sys.version_info[0]) + "." + str(sys.version_info[1]))'
}

prepare() {
  cd "${srcdir}/${pkgname}"
  git submodule update --init --recursive
  # fix build with protobuf 3.11, see https://github.com/onnx/onnx/pull/2482/files
  sed -i 's/${ONNX_DLLEXPORT_STR}${CMAKE_CURRENT_BINARY_DIR})/${CMAKE_CURRENT_BINARY_DIR})/' "${srcdir}/${pkgname}/CMakeLists.txt"
}

build() {
  cd "${pkgname}"
  python setup.py build
}

check() {
  cd "${srcdir}/${pkgname}"
  PYTHONPATH="${PWD}/build/lib.linux-${CARCH}-$(get_pyver)" pytest -v
}

package() {
  cd "${pkgname}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
