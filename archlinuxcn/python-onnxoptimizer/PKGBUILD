# Maintainer: Chih-Hsuan Yen <yan12125@gmail.com>

pkgname=python-onnxoptimizer
pkgver=0.2.7
pkgdesc='ONNX model optimizer'
pkgrel=1
arch=(x86_64)
url='https://github.com/onnx/optimizer'
license=(MIT)
depends=(python python-onnx)
makedepends=(python-setuptools cmake pybind11 git)
checkdepends=(python-pytest python-nbval python-onnxruntime
  # Disable tests using torchvision for now due to a pytorch bug
  # https://bugs.archlinux.org/task/74593
  # python-torchvision
)
source=("onnx-optimizer::git+https://github.com/onnx/optimizer.git#tag=v$pkgver"
        "git+https://github.com/onnx/onnx.git")
sha256sums=('SKIP'
            'SKIP')

prepare() {
  cd onnx-optimizer
  sed -i '/pytest-runner/d' setup.py
  # Use system protobuf
  sed -i '/third_party\/protobuf/d' CMakeLists.txt

  git submodule init
  git config submodule.third_party/onnx.url "$srcdir"/onnx
  git submodule update third_party/onnx
}

build() {
  cd onnx-optimizer
  # https://github.com/onnx/optimizer/issues/38
  CMAKE_ARGS="-DONNX_USE_LITE_PROTO=ON" python setup.py build
}

check() {
  cd onnx-optimizer
  pyver=$(python -c 'import sys; print(str(sys.version_info[0]) + "." + str(sys.version_info[1]))')
  PYTHONPATH="$PWD/build/lib.linux-$CARCH-$pyver" pytest
}

package() {
  cd onnx-optimizer
  python setup.py install --root="$pkgdir" --skip-build --optimize=1
  install -Dm644 LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname
}
