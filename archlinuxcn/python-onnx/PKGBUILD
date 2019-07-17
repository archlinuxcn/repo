# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-onnx
pkgver=1.5.0
pkgrel=4
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
source=("${pkgname}::git+https://github.com/onnx/onnx.git#tag=v${pkgver}"
        'no-typing.patch')
sha512sums=('SKIP'
            '902df9eb236f69c47d838813687fa8f22fee0efeea6a831a9ed0c78c8f52d93e31c57689141c92a8eb1a4c3592a8e01162c857b72766543a9e1a8f43b1b0efe7')

prepare() {
  cd "${srcdir}/${pkgname}"
  git submodule update --init --recursive
  patch -Np1 -i ../no-typing.patch
}

build() {
  cd "${pkgname}"
  python setup.py build
}

check() {
  cd "${srcdir}/${pkgname}"
  PYTHONPATH=$(pwd)/build/lib.linux-$CARCH-3.7 pytest -v
}

package() {
  cd "${pkgname}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
