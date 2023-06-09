# Maintainer: Butui Hu <hot123tea123@gmail.com>

_CUDA_ARCH_LIST="6.0;6.1;6.2;7.0;7.2;7.5;8.0;8.6;8.6;8.9;9.0;9.0+PTX"
pkgname=python-monai
_pkgname=MONAI
pkgver=1.2.0
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
sha512sums=('d7fec96248933dd73f992eb6acd37b95acea261cb352e1e6af8fbe0975c59284e40fb59dda2a7c764504c97367e77aae027574a73437e3d0a91f531520db9694')

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
