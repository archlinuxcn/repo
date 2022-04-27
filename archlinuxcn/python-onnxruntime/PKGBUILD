# Maintainer: Chih-Hsuan Yen <yan12125@gmail.com>

pkgbase=python-onnxruntime
# Not split DNNL EP to another package as it's needed unconditionally at runtime if built at compile time
# https://github.com/microsoft/onnxruntime/blob/v1.9.1/onnxruntime/python/onnxruntime_pybind_state.cc#L533
pkgname=(python-onnxruntime python-onnxruntime-cuda)
pkgver=1.11.1
pkgdesc='Cross-platform, high performance scoring engine for ML models'
pkgrel=1
arch=(x86_64)
url='https://github.com/microsoft/onnxruntime'
license=(MIT)
depends=(nsync re2 python-flatbuffers python-numpy python-protobuf openmpi onednn libprotobuf-lite.so)
makedepends=(git cmake pybind11 python-setuptools nlohmann-json chrono-date boost eigen flatbuffers cuda cudnn nccl)
optdepends=(
  # https://github.com/microsoft/onnxruntime/pull/9969
  'python-onnx: for the backend API, quantization, orttraining, transformers and various tools'
  'python-coloredlogs: for transformers'  # also used by TensorRT tools, but we don't build for it, anyway
  'python-psutil: for transformers'
  'python-py-cpuinfo: for transformers'
  'python-py3nvml: for transformers'
  'python-packaging: for transformers and various tools'
  'python-transformers: for transformers'
  'python-scipy: for transformers and various tools'
  'python-pytorch: for transformers, orttraining and various tools'
  'python-cerberus: for orttraining'
  'python-h5py: for orttraining'
  'python-sympy: for transformers and various tools'
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
        protobuf-3.20.diff
        system-dnnl.diff)
sha512sums=('SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            '80ea85ea20bbbdec7991f965a66b627a5f42828bc0c72be0913078d927833a82402fb1af6c5c9f6ecae861b45582fa42c98ce83b02768e4bf875ab89dd1c607c'
            '06a002361cc324184d0bfcb520b472f57749c0537329f0e0dee833cc7fce2f08b14590b77bc0211422dfb933dbef6f249f19939f9e0df465c48ee8fc7827e31c'
            '5b1b5c20efb2df48c651b957824d497e5465b2e572c9f12bf43546301ecc55f3ff5bb1004b491283a3957c18ff23220bad664dbcf6bcab9dc38cd77cdac30f6e'
            '6735c7aca2ba2f1f2a5286eb064125bf7f2c68a575d572dd157769d15778ff3e717b3a53d696c767748229f23ee6c3a7c82679df1d86283d7c4dd0ec9103ae08')
# CUDA seems not working with LTO
options+=('!lto')

# Check PKGBUILDs of python-pytorch and tensorflow for CUDA architectures built by official packages
_CUDA_ARCHITECTURES="52-real;53-real;60-real;61-real;62-real;70-real;72-real;75-real;80-real;86-real;86-virtual"

prepare() {
  cd onnxruntime

  patch -Np1 -i ../build-fixes.patch
  patch -Np1 -i ../install-orttraining-files.diff
  patch -Np1 -i ../protobuf-3.20.diff
  patch -Np1 -i ../system-dnnl.diff

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
