# Maintainer: Chih-Hsuan Yen <yan12125@gmail.com>

pkgbase=python-onnxruntime
# Not split DNNL EP to another package as it's needed unconditionally at runtime if built at compile time
# https://github.com/microsoft/onnxruntime/blob/v1.9.1/onnxruntime/python/onnxruntime_pybind_state.cc#L533
pkgname=(python-onnxruntime python-onnxruntime-cuda)
pkgver=1.9.1
pkgdesc='Cross-platform, high performance scoring engine for ML models'
pkgrel=4
arch=(x86_64)
url='https://github.com/microsoft/onnxruntime'
license=(MIT)
depends=(nsync re2 python-flatbuffers python-numpy python-onnx python-protobuf openmpi onednn)
makedepends=(git cmake gtest gmock pybind11 python-setuptools nlohmann-json chrono-date boost eigen flatbuffers cuda cudnn nccl clang)
# not de-vendored libraries
# onnx: needs shared libonnx (https://github.com/onnx/onnx/issues/3030)
source=("git+https://github.com/microsoft/onnxruntime#tag=v$pkgver"
        "git+https://github.com/onnx/onnx.git"
        "git+https://github.com/dcleblanc/SafeInt.git"
        "git+https://github.com/martinmoene/optional-lite.git"
        "git+https://github.com/tensorflow/tensorboard.git"
        "git+https://github.com/dmlc/dlpack.git"
        "git+https://github.com/jarro2783/cxxopts.git"
        "pytorch_cpuinfo::git+https://github.com/pytorch/cpuinfo.git"
        build-fixes.patch
        clang.patch
        system-dnnl.diff)
sha512sums=('SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            '685f0235abed6e1277dd0eb9bda56c464d1987fe7fc90a3550e17ec70cc49fd15f34996a0e159f9622c4ca3e6bf29917fe51b7849342531fa2a6808d782f1e06'
            'ad94af8bb25744b244c4f82e9a06189741f82b295a88523ca0e8005568fac710c2299d783989457e9cf96ef8da0593fb4f70c8792d416f44ab29d6493e204f13'
            '6735c7aca2ba2f1f2a5286eb064125bf7f2c68a575d572dd157769d15778ff3e717b3a53d696c767748229f23ee6c3a7c82679df1d86283d7c4dd0ec9103ae08')
# CUDA seems not working with LTO
options+=('!lto')

# Check PKGBUILDs of python-pytorch and tensorflow for CUDA architectures built by official packages
_CUDA_ARCHITECTURES="52-real;53-real;60-real;61-real;62-real;70-real;72-real;75-real;80-real;86-real;86-virtual"

prepare() {
  cd onnxruntime

  patch -Np1 -i ../build-fixes.patch
  patch -Np1 -i ../clang.patch
  patch -Np1 -i ../system-dnnl.diff

  git submodule init
  for mod in onnx SafeInt optional-lite tensorboard dlpack cxxopts pytorch_cpuinfo; do
    git config submodule.cmake/external/$mod.url "$srcdir"/$mod
    git submodule update cmake/external/$mod
  done
}

build() {
  cd "$srcdir"/onnxruntime

  local cmake_args=(
    -DCMAKE_INSTALL_PREFIX=/usr
    -Donnxruntime_ENABLE_PYTHON=ON
    -Donnxruntime_PREFER_SYSTEM_LIB=ON
    -Donnxruntime_BUILD_SHARED_LIB=ON
    -Donnxruntime_ENABLE_TRAINING=ON
    -Donnxruntime_USE_MPI=ON
    -Donnxruntime_USE_PREINSTALLED_EIGEN=ON
    -Donnxruntime_USE_DNNL=ON
    -Deigen_SOURCE_PATH=/usr/include/eigen3
  )

  # Use protobuf-lite instead of full protobuf to workaround symbol conflicts
  # with onnx; see https://github.com/onnx/onnx/issues/1277 for details.
  cmake_args+=(
    -DONNX_CUSTOM_PROTOC_EXECUTABLE=/usr/bin/protoc
    -Donnxruntime_USE_FULL_PROTOBUF=OFF
  )

  # 1. Redefine ___is_signed to ___is_signed to workaround a regression
  #    from CUDA 11.3 -> 11.3.1 [1].
  # 2. Enable parallel builds for NVCC via -t0, which spawns multiple
  #    cicc and ptxas processes for each nvcc invocation. The number of
  #    total processes may be much larger than the number of cores - let
  #    the scheduler handle it.
  # [1] https://forums.developer.nvidia.com/t/182176
  cmake_args+=(
    -DCMAKE_CUDA_HOST_COMPILER=/usr/bin/clang
    -DCMAKE_CUDA_FLAGS="-D__is_signed=___is_signed -t0"
    -DCMAKE_CUDA_ARCHITECTURES="$_CUDA_ARCHITECTURES"
    -Donnxruntime_USE_CUDA=ON
    -Donnxruntime_CUDA_HOME=/opt/cuda
    -Donnxruntime_CUDNN_HOME=/usr
    -Donnxruntime_USE_NCCL=ON
  )

  # Use clang as GCC does not work. GCC 11 crashes with internal
  # compiler errors. GCC 10 does not work as some dependent packages
  # (ex: re2) are built with libstdc++ from GCC 11, and thus linking
  # onnxruntime with libstdc++ 10 fails.
  CC=/usr/bin/clang CXX=/usr/bin/clang++ \
    cmake -B build -S cmake "${cmake_args[@]}" "$@"

  cd build
  make
  python ../setup.py build
}

package_python-onnxruntime() {
  cd onnxruntime/build

  make install DESTDIR="$pkgdir"

  python ../setup.py install --root="$pkgdir" --skip-build --optimize=1

  PY_ORT_DIR="$(python -c 'import site; print(site.getsitepackages()[0])')/onnxruntime"
  install -Ddm755 "$pkgdir"/usr/share/licenses/$pkgname
  for f in LICENSE ThirdPartyNotices.txt ; do
    ln -s "$PY_ORT_DIR/$f" "$pkgdir"/usr/share/licenses/$pkgname/$f
  done
  # already installed by `make install`, and not useful as this path is not looked up by the linker
  rm -vf "$pkgdir/$PY_ORT_DIR"/capi/libonnxruntime_providers_*

  # installed as split packages
  rm -vf "$pkgdir"/usr/lib/libonnxruntime_providers_cuda.so
}

package_python-onnxruntime-cuda() {
  depends+=(cuda cudnn nccl python-onnxruntime)
  pkgdesc+=' (CUDA execution provider)'

  cd onnxruntime/build
  install -Dm755 libonnxruntime_providers_cuda.so -t "$pkgdir"/usr/lib
  install -Ddm755 "$pkgdir"/usr/share/licenses
  ln -s python-onnxruntime "$pkgdir"/usr/share/licenses/$pkgname
}
