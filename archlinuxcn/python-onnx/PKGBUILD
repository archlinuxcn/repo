# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-onnx
pkgver=1.5.0
pkgrel=2
pkgdesc='Open Neural Network Exchange'
arch=('x86_64')
url='https://onnx.ai'
license=('MIT')
depends=(
  'protobuf'
  'python-numpy'
  'python-six'
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

prepare() {
  cd "${srcdir}/${pkgname}"
  git submodule update --init --recursive
}

build() {
  cd "${pkgname}"
  python setup.py build
}

check() {
  cd "${srcdir}/${pkgname}"
  pytest -v
}

package() {
  cd "${pkgname}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
