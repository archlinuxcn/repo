# Maintainer: Chih-Hsuan Yen <yan12125@gmail.com>

pkgbase=python-onnxruntime
# Not split DNNL EP to another package as it's needed unconditionally at runtime if built at compile time
# https://github.com/microsoft/onnxruntime/blob/v1.9.1/onnxruntime/python/onnxruntime_pybind_state.cc#L533
pkgname=(python-onnxruntime python-onnxruntime-cuda)
pkgver=1.10.0
pkgdesc='Cross-platform, high performance scoring engine for ML models'
pkgrel=4
arch=(x86_64)
url='https://github.com/microsoft/onnxruntime'
license=(MIT)
depends=(nsync re2 python-flatbuffers python-numpy python-protobuf openmpi onednn)
makedepends=(git cmake pybind11 python-setuptools nlohmann-json chrono-date boost eigen flatbuffers cuda cudnn nccl clang)
optdepends=(
  # https://github.com/microsoft/onnxruntime/pull/9969
  'python-onnx: for the backend API and transformers'
)
# not de-vendored libraries
# onnx: needs shared libonnx (https://github.com/onnx/onnx/issues/3030)
source=("git+https://github.com/microsoft/onnxruntime#tag=v$pkgver"
        "git+https://github.com/onnx/onnx.git"
        "git+https://github.com/dcleblanc/SafeInt.git"
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
            '80ea85ea20bbbdec7991f965a66b627a5f42828bc0c72be0913078d927833a82402fb1af6c5c9f6ecae861b45582fa42c98ce83b02768e4bf875ab89dd1c607c'
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
  # Fix building DNNL EP with clang https://github.com/microsoft/onnxruntime/pull/10014
  git cherry-pick -n c2d08a877b1f661eb99a29a57fd4184aa0918a80

  git submodule init
  for mod in onnx SafeInt tensorboard dlpack cxxopts pytorch_cpuinfo; do
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
    -Donnxruntime_BUILD_UNIT_TESTS=OFF
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
  # 3. Work-around the "error: type-id cannot have a name" issue with
  #    -DCMAKE_CUDA_STANDARD_REQUIRED=ON, which forces -std= to be
  #    specified [2].
  #
  #    $ echo "#include <type_traits>" | nvcc -ccbin /usr/bin/clang -x cu -c - -o /dev/null -v --keep
  #    /usr/bin/../lib64/gcc/x86_64-pc-linux-gnu/11.1.0/../../../../include/c++/11.1.0/type_traits:591:162: error: type-id cannot have a name
  #    template< class _Tp> using __is_signed_integer = __is_one_of< __remove_cv_t< _Tp> , signed char, signed short, signed int, signed long, signed long long, signed __int128_t> ;
  #                                                                                                                                                                      ^
  #    1 error generated.
  #
  #    It is a clang bug exposed by CMake and CUDA. Since CMake 3.22,
  #    -std= flag is no longer specified to nvcc (related to
  #    CMP0128 [3] ?). On the other hand, when no -std= option is
  #    specified, clang defines -D__GLIBCXX_TYPE_INT_N_0=__int128, and
  #    cudafe++ somehow replaces __int128 with __int128_t, which does
  #    not work with signed/unsigned in clang.
  # [1] https://forums.developer.nvidia.com/t/182176
  # [2] https://cmake.org/cmake/help/latest/prop_tgt/LANG_STANDARD_REQUIRED.html
  # [3] https://cmake.org/cmake/help/latest/policy/CMP0128.html
  cmake_args+=(
    -DCMAKE_CUDA_HOST_COMPILER=/usr/bin/clang
    -DCMAKE_CUDA_FLAGS="-D__is_signed=___is_signed -t0"
    -DCMAKE_CUDA_ARCHITECTURES="$_CUDA_ARCHITECTURES"
    -DCMAKE_CUDA_STANDARD_REQUIRED=ON
    -Donnxruntime_USE_CUDA=ON
    -Donnxruntime_CUDA_HOME=/opt/cuda
    -DCMAKE_CUDA_COMPILER:PATH=/opt/cuda/bin/nvcc
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
