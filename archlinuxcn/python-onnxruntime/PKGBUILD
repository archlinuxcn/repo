# Maintainer: Chih-Hsuan Yen <yan12125@gmail.com>

pkgbase=python-onnxruntime
pkgname=(python-onnxruntime python-onnxruntime-cuda)
pkgver=1.2.0
pkgdesc='Cross-platform, high performance scoring engine for ML models'
pkgrel=4
arch=(x86_64)
url='https://github.com/microsoft/onnxruntime'
license=(MIT)
depends=(protobuf re2 python-numpy)
makedepends=(git cmake cuda cudnn gtest gmock pybind11 python-setuptools cub nlohmann-json chrono-date)
# not de-vendored libraries
# eigen: API changes a lot since extra/eigen 3.3.7 to the commit onnxruntime uses
# onnx: onnxruntime uses different protobuf files than upstream onnx
# https://github.com/microsoft/onnxruntime/blob/v1.1.2/onnxruntime/core/protobuf/onnx-ml.proto#L250-L251
source=("git+https://github.com/microsoft/onnxruntime#tag=v$pkgver"
        "git+https://gitlab.com/libeigen/eigen.git"
        "git+https://github.com/google/gemmlowp.git"
        "git+https://github.com/google/nsync.git"
        "git+https://github.com/onnx/onnx.git"
        "git+https://github.com/dcleblanc/SafeInt.git"
        build-fixes.patch
        cmake-3.17.patch::https://github.com/microsoft/onnxruntime/commit/355f39ddee885237bf6fde9b587c7a5f80d22c53.patch)
sha512sums=('SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            '4457e19e3e91195ea2976a70e31a70d07b1b5e2279f1493a537c7d128aef5695e317cfdb84a87a0ca8d2d53ba15d72edf0f95905ecff7fbfb250e3a97944313c'
            '8804a5ecda6c5b2a341a723e918fc06f1e64a4500ea8fef835e76cca99ba4aba91465f2ddde8aac99ddf759bfa022a9b18641f9ec17c8592ec9e82eac69edef1')

prepare() {
  cd onnxruntime

  # More protobuf debundling; inspired by https://github.com/microsoft/onnxruntime/pull/1928
  rm -v onnxruntime/core/util/protobuf_parsing_utils.h
  echo "#include <google/protobuf/io/zero_copy_stream_impl.h>" >> onnxruntime/core/util/protobuf_parsing_utils.h
  patch -Np1 -i ../build-fixes.patch
  patch -Np1 -i ../cmake-3.17.patch

  git submodule init
  for mod in eigen gemmlowp nsync onnx SafeInt; do
    git config submodule.cmake/external/$mod.url "$srcdir"/$mod
    git submodule update cmake/external/$mod
  done

  mkdir build build-cuda
}

_build() {
  # Use protobuf-lite instead of full protobuf to workaround symbol conflicts
  # with onnx; see https://github.com/onnx/onnx/issues/1277 for details.
  cmake ../cmake \
    -Donnxruntime_ENABLE_PYTHON=ON \
    -DONNX_CUSTOM_PROTOC_EXECUTABLE=/usr/bin/protoc \
    -Donnxruntime_PREFER_SYSTEM_LIB=ON \
    -Donnxruntime_USE_FULL_PROTOBUF=OFF \
    $@
  make
  python ../setup.py build
}

build() {
  cd "$srcdir"/onnxruntime/build
  _build

  cd "$srcdir"/onnxruntime/build-cuda
  # Uses the same compiler as CUDA, or there will be linker errors due to
  # attempts on linking object files with libstdc++ from older GCC
  CC=/opt/cuda/bin/gcc CXX=/opt/cuda/bin/g++ \
  _build -Donnxruntime_USE_CUDA=ON -Donnxruntime_CUDNN_HOME=/usr
}

check() {
  cd "$srcdir"/onnxruntime/build
  make test

  cd "$srcdir"/onnxruntime/build-cuda
  # make test  # requires machines with CUDA-compatible devices
}

_package() {
  python ../setup.py install --root="$pkgdir" --skip-build --optimize=1

  PY_SITE_DIR="$(python -c 'import site; print(site.getsitepackages()[0])')"
  install -Ddm755 "$pkgdir"/usr/share/licenses/$pkgname
  for f in LICENSE ThirdPartyNotices.txt ; do
    ln -s "$PY_SITE_DIR/onnxruntime/$f" "$pkgdir"/usr/share/licenses/$pkgname/$f
  done
}

package_python-onnxruntime() {
  cd onnxruntime/build
  _package
}

package_python-onnxruntime-cuda() {
  depends+=(cuda cudnn)
  conflicts=(python-onnxruntime)
  provides=("python-onnxruntime=$pkgver")

  cd onnxruntime/build-cuda
  _package
}
