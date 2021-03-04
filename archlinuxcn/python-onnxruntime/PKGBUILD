# Maintainer: Chih-Hsuan Yen <yan12125@gmail.com>

pkgname=python-onnxruntime
pkgver=1.7.0
pkgdesc='Cross-platform, high performance scoring engine for ML models'
pkgrel=2
arch=(x86_64)
url='https://github.com/microsoft/onnxruntime'
license=(MIT)
depends=(nsync re2 flatbuffers python-numpy python-onnx python-protobuf)
makedepends=(git cmake gtest gmock pybind11 python-setuptools nlohmann-json chrono-date boost)
# not de-vendored libraries
# eigen: API changes a lot since extra/eigen 3.3.7 to the commit onnxruntime uses
# onnx: needs shared libonnx (https://github.com/onnx/onnx/issues/3030)
# https://github.com/microsoft/onnxruntime/blob/v1.1.2/onnxruntime/core/protobuf/onnx-ml.proto#L250-L251
source=("git+https://github.com/microsoft/onnxruntime#tag=v$pkgver"
        "git+https://gitlab.com/libeigen/eigen.git"
        "git+https://github.com/onnx/onnx.git"
        "git+https://github.com/dcleblanc/SafeInt.git"
        "git+https://github.com/martinmoene/optional-lite.git"
        build-fixes.patch)
sha512sums=('SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            '90e67eb144770734b488bf8ac5ad0dc955d2d860d9ed1c32285ffe913e72d27a3ac5b27588f41042fa4008533234e6cf4740c600f2b3fdce90ef8a3f853827eb')

prepare() {
  cd onnxruntime

  patch -Np1 -i ../build-fixes.patch

  git submodule init
  for mod in eigen onnx SafeInt optional-lite; do
    git config submodule.cmake/external/$mod.url "$srcdir"/$mod
    git submodule update cmake/external/$mod
  done
}

build() {
  cd "$srcdir"/onnxruntime
  # Use protobuf-lite instead of full protobuf to workaround symbol conflicts
  # with onnx; see https://github.com/onnx/onnx/issues/1277 for details.
  cmake -B build -S cmake \
    -Donnxruntime_ENABLE_PYTHON=ON \
    -DONNX_CUSTOM_PROTOC_EXECUTABLE=/usr/bin/protoc \
    -Donnxruntime_PREFER_SYSTEM_LIB=ON \
    -Donnxruntime_USE_FULL_PROTOBUF=OFF

  cd build
  make
  python ../setup.py build
}

check() {
  cd onnxruntime/build
  make test
}

package() {
  cd onnxruntime/build
  python ../setup.py install --root="$pkgdir" --skip-build --optimize=1

  PY_SITE_DIR="$(python -c 'import site; print(site.getsitepackages()[0])')"
  install -Ddm755 "$pkgdir"/usr/share/licenses/$pkgname
  for f in LICENSE ThirdPartyNotices.txt ; do
    ln -s "$PY_SITE_DIR/onnxruntime/$f" "$pkgdir"/usr/share/licenses/$pkgname/$f
  done
}
