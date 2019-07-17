# Maintainer: Chih-Hsuan Yen <yan12125@gmail.com>

pkgbase=python-onnxruntime
pkgname=(python-onnxruntime python-onnxruntime-cuda)
pkgver=0.4.0
pkgdesc='Cross-platform, high performance scoring engine for ML models'
pkgrel=2
arch=(x86_64)
url='https://github.com/microsoft/onnxruntime'
license=(MIT)
depends=(protobuf re2 python-numpy)
# protobuf 3.7.0 has an issue, which breaks building of onnxruntime
# https://github.com/protocolbuffers/protobuf/issues/5869
makedepends=(git cmake cuda cudnn gtest gmock pybind11 python-setuptools 'protobuf>=3.7.1' )
# not de-vendored libraries
# eigen: API changes a lot since extra/eigen 3.3.7 to the commit onnxruntime uses
# onnx: onnxruntime requires headers, which are not installed in python-onnx
source=("git+https://github.com/microsoft/onnxruntime#tag=v$pkgver"
        "git+https://github.com/HowardHinnant/date.git"
        "eigen::git+https://github.com/eigenteam/eigen-git-mirror.git"
        "git+https://github.com/google/gemmlowp.git"
        "gsl::git+https://github.com/Microsoft/GSL.git"
        "git+https://github.com/google/nsync.git"
        "git+https://github.com/onnx/onnx.git"
        build-fixes.patch)
sha512sums=('SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            '4901a35f1c8687555c63aaa9d0dddab9becd59b4779dd1040c19bb7dcf690773df103cffac94228f7019644d0cca03c09df525b8188fc3eef65557af07e25a26')

prepare() {
  cd onnxruntime
  patch -Np1 -i ../build-fixes.patch

  git submodule init
  for mod in date eigen gemmlowp gsl nsync onnx ; do
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
