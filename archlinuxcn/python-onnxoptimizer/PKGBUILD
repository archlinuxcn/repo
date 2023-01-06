# Maintainer: Chih-Hsuan Yen <yan12125@gmail.com>

pkgname=python-onnxoptimizer
pkgver=0.3.6
pkgdesc='ONNX model optimizer'
pkgrel=1
arch=(x86_64)
url='https://github.com/onnx/optimizer'
license=(MIT)
depends=(python python-onnx)
makedepends=(python-setuptools cmake pybind11 git)
checkdepends=(python-pytest python-nbval python-onnxruntime python-torchvision)
source=("onnx-optimizer::git+https://github.com/onnx/optimizer.git#tag=v$pkgver"
        "onnx-daquexian"::"git+https://github.com/daquexian/onnx.git")
sha256sums=('SKIP'
            'SKIP')
options=('debug')

prepare() {
  cd onnx-optimizer
  sed -i '/pytest-runner/d' setup.py

  git submodule init
  git config submodule.third_party/onnx.url "$srcdir"/onnx-daquexian
  git -c protocol.file.allow=always submodule update third_party/onnx
}

build() {
  cd onnx-optimizer
  # Use system protobuf and protobuf-lite (https://github.com/onnx/optimizer/issues/38)
  CMAKE_ARGS="-DONNX_OPT_USE_SYSTEM_PROTOBUF=ON -DONNX_USE_PROTOBUF_SHARED_LIBS=ON -DONNX_USE_LITE_PROTO=ON" python setup.py build
}

check() {
  cd onnx-optimizer
  pyver=$(python -c 'import sys; print(str(sys.version_info[0]) + str(sys.version_info[1]))')
  PYTHONPATH="$PWD/build/lib.linux-$CARCH-cpython-$pyver" pytest
}

package() {
  cd onnx-optimizer
  python setup.py install --root="$pkgdir" --skip-build --optimize=1
  install -Dm644 LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname
}
