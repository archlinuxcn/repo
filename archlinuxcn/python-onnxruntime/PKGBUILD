# Maintainer: Chih-Hsuan Yen <yan12125@gmail.com>

_ENABLE_CUDA=1

pkgbase=python-onnxruntime
# Not split DNNL EP to another package as it's needed unconditionally at runtime if built at compile time
# https://github.com/microsoft/onnxruntime/blob/v1.9.1/onnxruntime/python/onnxruntime_pybind_state.cc#L533
pkgname=(python-onnxruntime)
pkgver=1.12.1
pkgdesc='Cross-platform, high performance scoring engine for ML models'
pkgrel=1
arch=(x86_64)
url='https://github.com/microsoft/onnxruntime'
license=(MIT)
depends=(nsync re2 openmpi onednn libprotobuf-lite.so
         python-coloredlogs python-flatbuffers python-numpy python-packaging python-protobuf python-sympy)
makedepends=(git cmake pybind11 python-setuptools nlohmann-json chrono-date boost eigen flatbuffers)
optdepends=(
  # https://github.com/microsoft/onnxruntime/pull/9969
  'python-onnx: for the backend API, quantization, orttraining, transformers and various tools'
  'python-psutil: for transformers'
  'python-py-cpuinfo: for transformers'
  'python-py3nvml: for transformers'
  'python-transformers: for transformers'
  'python-scipy: for transformers and various tools'
  'python-pytorch: for transformers, orttraining and various tools'
  'python-cerberus: for orttraining'
  'python-h5py: for orttraining'
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
        install-orttraining-files.diff
        system-dnnl.diff)
sha512sums=('SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'ab0446ede08e528ca631a73e536ff42009ee8f152972d37050b2f9b44b3d1c06d19bd8a91c31b09c26f5db1482a699b8fe2c221b78199199dfa245728856b196'
            '7d55b0d4232183a81c20a5049f259872150536eed799d81a15e7f10b5c8b5279b443ba96d7b97c0e4338e95fc18c9d6f088e348fc7002256ee7170d25b27d80d'
            '6735c7aca2ba2f1f2a5286eb064125bf7f2c68a575d572dd157769d15778ff3e717b3a53d696c767748229f23ee6c3a7c82679df1d86283d7c4dd0ec9103ae08')
# CUDA seems not working with LTO
options+=('!lto')

if [[ $_ENABLE_CUDA = 1 ]]; then
  pkgname+=(python-onnxruntime-cuda)
  makedepends+=(cuda cudnn nccl gcc11)
fi

# Check PKGBUILDs of python-pytorch and tensorflow for CUDA architectures built by official packages
_CUDA_ARCHITECTURES="52-real;53-real;60-real;61-real;62-real;70-real;72-real;75-real;80-real;86-real;86-virtual"

prepare() {
  cd onnxruntime

  patch -Np1 -i ../build-fixes.patch
  patch -Np1 -i ../install-orttraining-files.diff
  patch -Np1 -i ../system-dnnl.diff

  # Protobuf 3.20 incompatibility https://github.com/microsoft/onnxruntime/pull/11639
  git cherry-pick -n 6aa286f1e3ece96a7326ea55fdcd225f1ff8bbf2
  # Fix building DNNL EP with GCC 12 https://github.com/microsoft/onnxruntime/pull/11667
  git cherry-pick -n 59ca05cb1c1de0492d10ac895904b217c86e612d

  git submodule init
  for mod in onnx SafeInt tensorboard dlpack cxxopts pytorch_cpuinfo; do
    git config submodule.cmake/external/$mod.url "$srcdir"/$mod
    git submodule update cmake/external/$mod
  done

  cd onnxruntime/core/flatbuffers/schema
  python compile_schema.py --flatc /usr/bin/flatc
}

build() {
  cd "$srcdir"/onnxruntime

  if [[ $_ENABLE_CUDA = 1 ]]; then
    export CC=/usr/bin/gcc-11
    export CXX=/usr/bin/g++-11
    export CUDAHOSTCXX=$CXX
  fi

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

  if [[ $_ENABLE_CUDA = 1 ]]; then
    # 1. Enable parallel builds for NVCC via -t0, which spawns multiple
    #    cicc and ptxas processes for each nvcc invocation. The number of
    #    total processes may be much larger than the number of cores - let
    #    the scheduler handle it.
    cmake_args+=(
      -DCMAKE_CUDA_FLAGS="-t0"
      -DCMAKE_CUDA_ARCHITECTURES="$_CUDA_ARCHITECTURES"
      -DCMAKE_CUDA_STANDARD_REQUIRED=ON
      -DCMAKE_CXX_STANDARD_REQUIRED=ON
      -Donnxruntime_USE_CUDA=ON
      -Donnxruntime_CUDA_HOME=/opt/cuda
      -DCMAKE_CUDA_COMPILER:PATH=/opt/cuda/bin/nvcc
      -Donnxruntime_CUDNN_HOME=/usr
      -Donnxruntime_USE_NCCL=ON
    )
  fi

  cmake -B build -S cmake "${cmake_args[@]}" "$@"

  cd build
  cmake --build .
  python ../setup.py build
}

package_python-onnxruntime() {
  cd onnxruntime/build

  DESTDIR="$pkgdir" cmake --install .

  python ../setup.py install --root="$pkgdir" --skip-build --optimize=1

  PY_ORT_DIR="$(python -c 'import site; print(site.getsitepackages()[0])')/onnxruntime"
  install -Ddm755 "$pkgdir"/usr/share/licenses/$pkgname
  for f in LICENSE ThirdPartyNotices.txt ; do
    ln -s "$PY_ORT_DIR/$f" "$pkgdir"/usr/share/licenses/$pkgname/$f
  done
  # already installed by `cmake --install`, and not useful as this path is not looked up by the linker
  rm -vf "$pkgdir/$PY_ORT_DIR"/capi/libonnxruntime_providers_*

  # installed as split packages
  rm -vf "$pkgdir"/usr/lib/libonnxruntime_providers_cuda.so
}

package_python-onnxruntime-cuda() {
  depends=(cuda cudnn nccl openmpi nsync)
  pkgdesc+=' (CUDA execution provider)'

  cd onnxruntime/build
  install -Dm755 libonnxruntime_providers_cuda.so -t "$pkgdir"/usr/lib
  install -Ddm755 "$pkgdir"/usr/share/licenses
  ln -s python-onnxruntime "$pkgdir"/usr/share/licenses/$pkgname
}
