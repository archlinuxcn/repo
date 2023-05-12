# Maintainer: Butui Hu <hot123tea123@gmail.com>

_CUDA_ARCH_LIST="6.0;6.1;6.2;7.0;7.2;7.5;8.0;8.6;8.6;8.9;9.0;9.0+PTX"
pkgname=python-monai
_pkgname=MONAI
pkgver=1.1.0
pkgrel=3
pkgdesc='AI Toolkit for Healthcare Imaging'
arch=('any')
url='https://monai.io'
license=('Apache')
depends=(
  python-pytorch-cuda
  python-numpy
)
makedepends=(
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
sha512sums=('df6e19b43e9f39052eca3107bbb39f67fa9559c4ad5c2e838423a6d035a580b92a48c7d98bbb926a8cf742fdf5c03e7c105be0cc76f4a2c8debf97fba80ecf4b')

prepare() {
  # disable building MONAI extension due to nvcc issue
  export BUILD_MONAI=0
  export FORCE_CUDA=1
  export TORCH_CUDA_ARCH_LIST=${_CUDA_ARCH_LIST}
  export CC=/opt/cuda/bin/gcc
  export CXX=/opt/cuda/bin/g++
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
