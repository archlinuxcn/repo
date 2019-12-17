# Maintainer: Chih-Hsuan Yen <yan12125@gmail.com>

pkgbase=python-onnxruntime
pkgname=(python-onnxruntime python-onnxruntime-cuda)
pkgver=1.0.0
pkgdesc='Cross-platform, high performance scoring engine for ML models'
pkgrel=5
arch=(x86_64)
url='https://github.com/microsoft/onnxruntime'
license=(MIT)
depends=(protobuf re2 python-numpy)
makedepends=(git cmake cuda cudnn gtest gmock pybind11 python-setuptools cub)
# not de-vendored libraries
# eigen: API changes a lot since extra/eigen 3.3.7 to the commit onnxruntime uses
# onnx: onnxruntime requires headers, which are not installed in python-onnx
source=("git+https://github.com/microsoft/onnxruntime#tag=v$pkgver"
        "git+https://github.com/HowardHinnant/date.git"
        "eigen::git+https://github.com/eigenteam/eigen-git-mirror.git"
        "git+https://github.com/google/gemmlowp.git"
        "git+https://github.com/google/nsync.git"
        "git+https://github.com/onnx/onnx.git"
        build-fixes.patch)
sha512sums=('SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'da8e27ff0011fb207ee8a6f8675160eb85cb8711f01050fa7454234242af141951cb5bba52fa50b98cf8567b8faa973565dfef37f4daa2219a42cf26e03c86b5')

prepare() {
  cd onnxruntime

  # More protobuf debundling; inspired by https://github.com/microsoft/onnxruntime/pull/1928
  rm -v onnxruntime/core/util/protobuf_parsing_utils.{h,cc}
  echo "#include <google/protobuf/io/zero_copy_stream_impl.h>" >> onnxruntime/core/util/protobuf_parsing_utils.h
  patch -Np1 -i ../build-fixes.patch

  git submodule init
  for mod in date eigen gemmlowp nsync onnx ; do
    git config submodule.cmake/external/$mod.url "$srcdir"/$mod
    git submodule update cmake/external/$mod
  done

  mkdir build build-cuda
}

_build() {
  # Uses the same compiler as CUDA, or there will be linker errors due to
  # attempts on linking object files with libstdc++ from older GCC
  CC=/opt/cuda/bin/gcc CXX=/opt/cuda/bin/g++ \
  cmake ../cmake \
    -Donnxruntime_ENABLE_PYTHON=ON \
    -DONNX_CUSTOM_PROTOC_EXECUTABLE=/usr/bin/protoc \
    $@
  make
  python ../setup.py build
}

build() {
  cd "$srcdir"/onnxruntime/build
  _build

  cd "$srcdir"/onnxruntime/build-cuda
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
