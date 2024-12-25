# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=horovod
pkgname=python-horovod
pkgver=0.28.1
pkgrel=5
pkgdesc='Distributed training framework for TensorFlow, Keras, PyTorch, and Apache MXNet'
arch=('x86_64')
url='https://github.com/horovod/horovod'
license=('Apache-2.0')
depends=(
  cuda
  cudnn
  gcc-libs
  glibc
  nccl
  openmpi
  python
  python-cloudpickle
  python-h5py
  python-mpi4py
  python-numpy
  python-psutil
  python-pycparser
  python-scipy
  python-six
  python-tqdm
  python-yaml
)
makedepends=(
  cmake
  gcc13
  git
  python-build
  python-installer
  python-pytorch-cuda
  python-setuptools
  # python-tensorflow-cuda
  python-wheel
)
optdepends=(
  'python-pytorch-cuda: pytorch framework'
  # 'python-tensorflow-cuda: tensorflow framework'
)
source=("${_pkgname}-${pkgver}::git+https://github.com/horovod/horovod.git#tag=v${pkgver}"
        "0001-fix-building-with-torch-2.1.patch::https://github.com/horovod/horovod/pull/3998.patch"
        "0002-fix-building-torch-extension-with-glog.patch"
        "https://github.com/horovod/horovod/pull/3957.patch"
)
sha512sums=('28deae90009eab98aa1066a884f9eb1620d7e793b5dcda6b4397df56b2b25cadd2ade3bc440eb0f62162573c84901470e10ab4211f85de92faa910e71d6b9f04'
            '7c56b56e665e0590ced4366d71dcd5ed83cab7e2943b0548d0472ef19b5a051a9dcaa8800c417882b171acbe4dc5f745e1c876aabb0bb8564215ce121f14cf67'
            '52850f5e4f60122e0064307f0d5d5fb6781c8f77f0e54d4b9c306e98bd15d1edc1c670a1623653fb571332c74cb11d7ffd5a1b7e6fe3403f990cc96ca5ccf7c0'
            'd3f808a9b8cd887dfe4b117e6c715ad28b15083b59334001da565108c9764eaf8dda76c9ae9c507fcc06362effcc72f3d9c2fdb443db9d0c9c839073359db613')

prepare() {
  cd "${_pkgname}-${pkgver}"
  patch -p1 -i "${srcdir}/0001-fix-building-with-torch-2.1.patch"
  patch -p1 -i "${srcdir}/0002-fix-building-torch-extension-with-glog.patch"
  patch -p1 -i "${srcdir}/3957.patch"
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
  HOROVOD_WITH_TENSORFLOW=NO \
  CC=gcc-13 \
  CXX=g++-13 \
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
