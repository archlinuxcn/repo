# Maintainer: Chih-Hsuan Yen <yan12125@gmail.com>

pkgbase=python-onnxruntime
pkgname=(python-onnxruntime python-onnxruntime-cuda)
pkgver=1.9.1
pkgdesc='Cross-platform, high performance scoring engine for ML models'
pkgrel=1
arch=(x86_64)
url='https://github.com/microsoft/onnxruntime'
license=(MIT)
depends=(nsync re2 python-flatbuffers python-numpy python-onnx python-protobuf openmpi)
makedepends=(git cmake gtest gmock pybind11 python-setuptools nlohmann-json chrono-date boost eigen flatbuffers cuda cudnn nccl clang)
checkdepends=(python-pytest python-pytorch python-h5py python-pandas python-psutil python-tqdm python-sympy python-torchvision tensorboard python-cerberus)
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
        clang.patch)
sha512sums=('SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            '685f0235abed6e1277dd0eb9bda56c464d1987fe7fc90a3550e17ec70cc49fd15f34996a0e159f9622c4ca3e6bf29917fe51b7849342531fa2a6808d782f1e06'
            'ad94af8bb25744b244c4f82e9a06189741f82b295a88523ca0e8005568fac710c2299d783989457e9cf96ef8da0593fb4f70c8792d416f44ab29d6493e204f13')
# CUDA seems not working with LTO
options+=('!lto')

# Check PKGBUILDs of python-pytorch and tensorflow for CUDA architectures built by official packages
_CUDA_ARCHITECTURES="52-real;53-real;60-real;61-real;62-real;70-real;72-real;75-real;80-real;86-real;86-virtual"

prepare() {
  cd onnxruntime

  patch -Np1 -i ../build-fixes.patch
  patch -Np1 -i ../clang.patch

  # 1.9.0 is marked as 1.10.0 https://github.com/microsoft/onnxruntime/blob/v1.9.0/VERSION_NUMBER
  # Official wheels are not affected, though
  echo $pkgver > VERSION_NUMBER

  git submodule init
  for mod in onnx SafeInt optional-lite tensorboard dlpack cxxopts pytorch_cpuinfo; do
    git config submodule.cmake/external/$mod.url "$srcdir"/$mod
    git submodule update cmake/external/$mod
  done
}

_build() {
  build_dir=$1
  shift

  cd "$srcdir"/onnxruntime
  # Use protobuf-lite instead of full protobuf to workaround symbol conflicts
  # with onnx; see https://github.com/onnx/onnx/issues/1277 for details.
  CC=/usr/bin/clang CXX=/usr/bin/clang++ \
  cmake -B $build_dir -S cmake \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -Donnxruntime_ENABLE_PYTHON=ON \
    -DONNX_CUSTOM_PROTOC_EXECUTABLE=/usr/bin/protoc \
    -Donnxruntime_PREFER_SYSTEM_LIB=ON \
    -Donnxruntime_USE_FULL_PROTOBUF=OFF \
    -Donnxruntime_BUILD_SHARED_LIB=ON \
    -Donnxruntime_ENABLE_TRAINING=ON \
    -Donnxruntime_USE_MPI=ON \
    -Donnxruntime_USE_PREINSTALLED_EIGEN=ON \
    -Deigen_SOURCE_PATH=/usr/include/eigen3 \
    "$@"

  cd $build_dir
  make
  python ../setup.py build
}

build() {
  _build build

  # 1. Use clang as GCC does not work. GCC 11 crashes with internal
  #    compiler errors. GCC 10 does not work as some dependent packages
  #    (ex: re2) are built with libstdc++ from GCC 11, and thus linking
  #    onnxruntime with libstdc++ 10 fails.
  # 2. Redefine ___is_signed to ___is_signed to workaround a regression
  #    from CUDA 11.3 -> 11.3.1 [1].
  # [1] https://forums.developer.nvidia.com/t/182176
  _build build-cuda \
    -DCMAKE_CUDA_HOST_COMPILER=/usr/bin/clang \
    -DCMAKE_CUDA_FLAGS="-D__is_signed=___is_signed" \
    -DCMAKE_CUDA_ARCHITECTURES="$_CUDA_ARCHITECTURES" \
    -Donnxruntime_USE_CUDA=ON \
    -Donnxruntime_CUDA_HOME=/opt/cuda \
    -Donnxruntime_CUDNN_HOME=/usr \
    -Donnxruntime_USE_NCCL=ON
}

_check() {
  # Test models are no longer publicly available [1]
  # [1] https://github.com/microsoft/onnxruntime/issues/7447
  GTEST_FILTER='-*ModelTest*' ARGS="--rerun-failed --output-on-failure" make test
  # launch_test.py seems a script, and orttraining_* include BERT tests, which require the
  # transformers package, and failed even if the latter is installed.

  # XXX: Some python tests failed (ex: [1]). In those tests, tested ONNX models are
  # generated on the fly using the onnx python library (ex: [2]). When the latter
  # is newer than the included onnx submodule, loading a tested ONNX model may fail
  # as the IR version for a tested model may be higher than the IR version used in
  # onnxruntime.
  # [1] https://build.archlinuxcn.org/~imlonghao/log/python-onnxruntime/2021-08-07T12%3A17%3A01.html
  # [2] https://github.com/microsoft/onnxruntime/blob/v1.8.2/onnxruntime/test/python/quantization/test_op_gemm.py#L28-L76
  LD_LIBRARY_PATH="$PWD" pytest \
    --ignore launch_test.py \
    --ignore orttraining_run_bert_pretrain.py \
    --ignore orttraining_run_frontend_batch_size_test.py \
    --ignore transformers
}

check() {
  cd "$srcdir"/onnxruntime/build
  _check

  cd "$srcdir"/onnxruntime/build-cuda
  # _check # requires machines with CUDA-compatible devices
}

_package() {
  make install DESTDIR="$pkgdir"

  python ../setup.py install --root="$pkgdir" --skip-build --optimize=1

  PY_ORT_DIR="$(python -c 'import site; print(site.getsitepackages()[0])')/onnxruntime"
  install -Ddm755 "$pkgdir"/usr/share/licenses/$pkgname
  for f in LICENSE ThirdPartyNotices.txt ; do
    ln -s "$PY_ORT_DIR/$f" "$pkgdir"/usr/share/licenses/$pkgname/$f
  done
  # already installed by `make install`, and not useful as this path is not looked up by the linker
  rm -vf "$pkgdir/$PY_ORT_DIR"/capi/libonnxruntime_providers_*
}

package_python-onnxruntime() {
  cd onnxruntime/build
  _package
}

package_python-onnxruntime-cuda() {
  depends+=(cuda cudnn nccl)
  conflicts=(python-onnxruntime)
  provides=("python-onnxruntime=$pkgver")

  cd onnxruntime/build-cuda
  _package
}
