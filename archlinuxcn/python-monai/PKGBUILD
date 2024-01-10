# Maintainer: Butui Hu <hot123tea123@gmail.com>

_CUDA_ARCH_LIST="6.0;6.1;6.2;7.0;7.2;7.5;8.0;8.6;8.6;8.9;9.0;9.0+PTX"
pkgname=python-monai
_pkgname=MONAI
pkgver=1.3.0
pkgrel=1
pkgdesc='AI Toolkit for Healthcare Imaging'
arch=('x86_64')
url='https://monai.io'
license=('Apache')
depends=(
  python-pytorch-cuda
  python-numpy
)
makedepends=(
  gcc10
  python-build
  python-installer
  python-setuptools
  python-wheel
)
optdepends=(
  gdown
  python-einops
  python-lmdb
  python-mlflow
  python-nibabel
  python-pandas
  python-parameterized
  python-pillow
  python-psutil
  python-pytorch-ignite
  python-scikit-image
  python-torchvision-cuda
  python-tqdm
  python-transformers
  tensorboard
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/Project-MONAI/MONAI/archive/refs/tags/${pkgver}.tar.gz")
sha512sums=('78c96361ac204cf9199e2c332d2a1751e7e3fb01edfd09e96ef68b3ecf0cea548eb4151dc5d064342397a970a8b8a8815427a7dbe0e39aaeb96f69505c7adba1')

prepare() {
  # disable building MONAI extension due to nvcc issue
  export BUILD_MONAI=1
  export FORCE_CUDA=1
  export TORCH_CUDA_ARCH_LIST=${_CUDA_ARCH_LIST}
  export CC=gcc-10
  export CXX=g++-10
}

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation -x
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
}
# vim:set ts=2 sw=2 et:
