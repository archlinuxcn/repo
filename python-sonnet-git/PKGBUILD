# Maintainer: Sasasu <lizhaolong0123@gmail.com>
pkgbase=python-sonnet-git
pkgname=(python-sonnet-git python-sonnet-cuda-git)
pkgver=20180531.170829
tf_pkgver=1.8.0
pkgrel=1
pkgdesc="TensorFlow-based neural network library."
url="https://github.com/deepmind/sonnet"
license=('Apache2')
arch=('x86_64')
depends=('python-tensorflow' 'python')
makedepends=('bazel' 'python-numpy' 'cuda' 'nvidia-utils'
             'cudnn' 'python-pip' 'python-wheel' 'python-setuptools'
             'git')
source=("git+https://github.com/deepmind/sonnet"
        "https://github.com/tensorflow/tensorflow/archive/v${tf_pkgver}.tar.gz")
sha512sums=('SKIP'
            '7280e65d26fb3f15d95f7217ee3bc08d1424cd144cf25bf638fa114fa835b2505dfaf457c55700067d24f485b77120973d094ec568e6d1b1054857402f9c352d')

prepare() {
  cp -r tensorflow-${tf_pkgver} tensorflow-${tf_pkgver}-cuda
  mkdir -p $srcdir/sonnet/tensorflow
  cp -r tensorflow-$tf_pkgver/* $srcdir/sonnet/tensorflow/
  cp -r $srcdir/sonnet $srcdir/sonnet-cuda
  # These environment variables influence the behavior of the configure call below.
  export PYTHON_BIN_PATH=/usr/bin/python
  export USE_DEFAULT_PYTHON_LIB_PATH=1
  export TF_NEED_JEMALLOC=1
  export TF_NEED_KAFKA=0
  export TF_NEED_OPENCL_SYCL=0
  export TF_NEED_GCP=0
  export TF_NEED_HDFS=0
  export TF_NEED_S3=0
  export TF_ENABLE_XLA=1
  export TF_NEED_GDR=0
  export TF_NEED_VERBS=0
  export TF_NEED_OPENCL=0
  export TF_NEED_MPI=0
  export TF_NEED_TENSORRT=0
  export TF_SET_ANDROID_WORKSPACE=0
  export TF_DOWNLOAD_CLANG=0
  export TF_NCCL_VERSION=1.3  # configure.py: _DEFAULT_NCCL_VERSION
  export GCC_HOST_COMPILER_PATH=/usr/bin/gcc
}

configure_tensorflow() {
  cd $srcdir/sonnet/tensorflow
  export CC_OPT_FLAGS="-march=x86-64"
  export TF_NEED_CUDA=0
  
  ./configure
}

configure_tensorflow_cuda() {
  cd $srcdir/sonnet-cuda/tensorflow
  export CC_OPT_FLAGS="-march=x86-64"
  export TF_NEED_CUDA=1
  export TF_CUDA_CLANG=0
  # export CLANG_CUDA_COMPILER_PATH=/usr/bin/clang
  export CUDA_TOOLKIT_PATH=/opt/cuda
  export TF_CUDA_VERSION=$($CUDA_TOOLKIT_PATH/bin/nvcc --version | sed -n 's/^.*release \(.*\),.*/\1/p')
  export CUDNN_INSTALL_PATH=/opt/cuda
  export TF_CUDNN_VERSION=$(sed -n 's/^#define CUDNN_MAJOR\s*\(.*\).*/\1/p' $CUDNN_INSTALL_PATH/include/cudnn.h)
  export TF_CUDA_COMPUTE_CAPABILITIES=3.0,3.5,5.2,6.1,6.2,7.0
  ./configure
}

build() {
  # CPU only
  cd $srcdir/sonnet/tensorflow
  msg2 "Configure tensorflow..."
  configure_tensorflow
  cd $srcdir/sonnet
  msg2 "Building sonnet ..."
  bazel build  --ignore_unsupported_sandboxing :install 
  mkdir -p tmp
  msg2 "Building pip package ..."
  ./bazel-bin/install $srcdir/sonnet python3
  
  # CUDA 
  cd $srcdir/sonnet-cuda/tensorflow
  msg2 "Configure tensorflow-cuda ..."
  configure_tensorflow_cuda
  cd $srcdir/sonnet-cuda
  msg2 "Building sonnet-cuda ..."
  bazel build  --ignore_unsupported_sandboxing :install 
  mkdir -p tmp
  msg2 "Building pip package ..."
  ./bazel-bin/install $srcdir/sonnet-cuda python3
}

package_python-sonnet-git() {
  cd "${srcdir}/sonnet"
  pip install --ignore-installed --upgrade --root "$pkgdir/" *.whl --no-dependencies
  install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
package_python-sonnet-cuda-git(){
  cd "${srcdir}/sonnet-cuda"
  pip install --ignore-installed --upgrade --root "$pkgdir/" *.whl --no-dependencies
  install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
# vim:set ts=2 sw=2 et:
