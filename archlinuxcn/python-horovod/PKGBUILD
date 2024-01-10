# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=horovod
pkgname=python-horovod
pkgver=0.28.1
pkgrel=2
pkgdesc='Distributed training framework for TensorFlow, Keras, PyTorch, and Apache MXNet'
arch=('x86_64')
url='https://github.com/horovod/horovod'
license=('Apache')
depends=(
  cuda
  cudnn
  nccl
  openmpi
  python-cloudpickle
  python-h5py
  python-mock
  python-mpi4py
  python-psutil
  python-pycparser
  python-pyaml
  python-scipy
  python-six
  python-tqdm
)
makedepends=(
  cmake
  git
  python-build
  python-installer
  python-pytorch-cuda
  python-setuptools
  python-tensorflow-cuda
  python-wheel
)
optdepends=(
  'python-pytorch-cuda: pytorch framework'
  'python-tensorflow-cuda: tensorflow framework'
)
source=("${_pkgname}-${pkgver}::git+https://github.com/horovod/horovod.git#tag=v${pkgver}"
        "0001.fix-building-with-torch-2.1.patch::https://github.com/horovod/horovod/pull/3998.patch"
)
sha512sums=('SKIP'
            '32ec82943a5f96de21b11b2b994f30779d827d8a5dab380654169eebc954e0dc122333d610fc32607a8bf11dd425117d035ab1f1cb8c6a36717c3c0b89692431')

prepare() {
  cd "${_pkgname}-${pkgver}"
  patch -p1 -i "${srcdir}/0001.fix-building-with-torch-2.1.patch"
  git submodule update --init --recursive
}

build() {
  cd "${_pkgname}-${pkgver}"
  # modify these environment variable as you need, see also https://github.com/horovod/horovod/blob/master/docs/install.rst
  HOROVOD_BUILD_CUDA_CC_LIST="60,61,62,70,72,75,80,86,89,90" \
  HOROVOD_CPU_OPERATIONS=GLOO \
  HOROVOD_CUDA_HOME=/opt/cuda \
  HOROVOD_GPU=CUDA \
  HOROVOD_GPU_OPERATIONS=NCCL \
  HOROVOD_NCCL_LINK=SHARED \
  HOROVOD_WITHOUT_MXNET=1 \
  HOROVOD_WITH_GLOO=1 \
  HOROVOD_WITH_MPI=1 \
  HOROVOD_WITH_PYTORCH=1 \
  HOROVOD_WITH_TENSORFLOW=1 \
  CC=/opt/cuda/bin/gcc \
  CXX=/opt/cuda/bin/g++ \
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:

