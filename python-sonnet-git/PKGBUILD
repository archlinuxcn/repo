# Maintainer: Sasasu <lizhaolong0123@gmail.com>
pkgbase=python-sonnet-git
# pkgname=(python-sonnet-git python-sonnet-cuda-git)
pkgname=(python-sonnet-git)
pkgver=20170515.170829
tf_pkgver=1.1.0
pkgrel=1
pkgdesc="TensorFlow-based neural network library."
url="https://github.com/deepmind/sonnet"
license=('Apache2')
arch=('x86_64')
depends=('python-tensorflow' 'python')
# makedepends=('git' 'bazel' 'python-numpy' 'gcc5' 'cuda' 'cudnn' 'python-pip' 'python-wheel' 'python-setuptools')
makedepends=('git' 'bazel' 'python-numpy' 'python-pip' 'python-wheel' 'python-setuptools')
source=("git+https://github.com/deepmind/sonnet"
        "https://github.com/tensorflow/tensorflow/archive/v${tf_pkgver}.tar.gz")
md5sums=('SKIP'
         'fb745649d33954c97d29b7acaffe7d65')

prepare() {
  mkdir -p $srcdir/sonnet/tensorflow
  cp -r tensorflow-$tf_pkgver/* $srcdir/sonnet/tensorflow/
  cp -r $srcdir/sonnet $srcdir/sonnet-cuda
  export PYTHON_BIN_PATH=/usr/bin/python
  export USE_DEFAULT_PYTHON_LIB_PATH=1
  export CC_OPT_FLAGS="-march=x86-64"
  export TF_NEED_JEMALLOC=1
  export TF_NEED_GCP=0
  export TF_NEED_HDFS=0
  export TF_ENABLE_XLA=1
  export TF_NEED_VERBS=0
  export TF_NEED_OPENCL=0
}

configure_tensorflow() {
  cd $srcdir/sonnet/tensorflow
  export TF_NEED_CUDA=0
  
  ./configure
}

configure_tensorflow_cuda() {
  cd $srcdir/sonnet/tensorflow
  export TF_NEED_CUDA=1
  export GCC_HOST_COMPILER_PATH=/usr/bin/gcc-5
  # For next version instead of the gcc-5 stuff:
  # export TF_CUDA_CLANG=1
  # export CLANG_CUDA_COMPILER_PATH=/usr/bin/clang
  export CUDA_TOOLKIT_PATH=/opt/cuda
  export TF_CUDA_VERSION=$($CUDA_TOOLKIT_PATH/bin/nvcc --version | sed -n 's/^.*release \(.*\),.*/\1/p')
  export CUDNN_INSTALL_PATH=/opt/cuda
  export TF_CUDNN_VERSION=$(sed -n 's/^#define CUDNN_MAJOR\s*\(.*\).*/\1/p' $CUDNN_INSTALL_PATH/include/cudnn.h)
  export TF_CUDA_COMPUTE_CAPABILITIES=3.0,3.5,5.2,6.1

  ./configure
}

build() {
  # CPU only
  cd $srcdir/sonnet/tensorflow
  msg2 "Configure tensorflow..."
  configure_tensorflow
  cd $srcdir/sonnet
  msg2 "Building sonnet ..."
  bazel build  --ignore_unsupported_sandboxing --config=opt :install 
  mkdir -p tmp
  msg2 "Building pip package ..."
  ./bazel-bin/install $srcdir/sonnet
  
  # CUDA 
  # no such target '@org_tensorflow//tensorflow/tools/git:gen/spec.json'
  # no such target '@org_tensorflow//tensorflow/tools/git:gen/head'
  # no such target '@org_tensorflow//tensorflow/tools/git:gen/branch_ref'
  # target '//:install' failed
  # Looks like a upstream problem 
  
  # cd $srcdir/sonnet-cuda/tensorflow
  # msg2 "Configure tensorflow-cuda ..."
  # configure_tensorflow_cuda
  # cd $srcdir/sonnet-cuda
  # msg2 "Building sonnet-cuda ..."
  # bazel build  --ignore_unsupported_sandboxing --config=opt :install 
  # mkdir -p tmp
  # msg2 "Building pip package ..."
  # ./bazel-bin/install $srcdir/sonnet-cuda
}

package_python-sonnet-git() {
  cd "${srcdir}/sonnet"
  PKG=$(find "$srcdir" -name "sonnet-*.whl")
  pip install --ignore-installed --upgrade --root "$pkgdir/" "$PKG" --no-dependencies
  install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
package_python-sonnet-cuda-git(){
  cd "${srcdir}/sonnet-cuda"
  PKG=$(find "$srcdir" -name "sonnet-*.whl")
  pip install --ignore-installed --upgrade --root "$pkgdir/" "$PKG" --no-dependencies
  install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
# vim:set ts=2 sw=2 et:

