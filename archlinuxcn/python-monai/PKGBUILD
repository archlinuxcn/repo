# Maintainer: Butui Hu <hot123tea123@gmail.com>

_CUDA_ARCH_LIST="5.2;5.3;6.0;6.1;6.2;7.0;7.2;7.5;8.0;8.6;8.6+PTX"
pkgname=python-monai
_pkgname=MONAI
pkgver=0.9.0rc2
pkgrel=1
pkgdesc='AI Toolkit for Healthcare Imaging'
arch=('x86_64')
url='https://monai.io'
license=('BSD')
depends=(
  python-pytorch-cuda
  python-numpy
)
makedepends=(
  gcc10
  python-pip
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
sha512sums=('cb1d5a63cde17142dc65866bd9341d4c307933891efcf91526291f723f21fe687e61d7c8e0ab1b4768a434cfedd1ccaf60d308ccb252a0b66a454cba94e01ea9')

build() {
  cd "${_pkgname}-${pkgver}"
  BUILD_MONAI=1 \
  CC=gcc-10 \
  CXX=g++-10 \
  FORCE_CUDA=1 \
  TORCH_CUDA_ARCH_LIST=${_CUDA_ARCH_LIST} \
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  BUILD_MONAI=1 \
  CC=gcc-10 \
  CXX=g++-10 \
  FORCE_CUDA=1 \
  TORCH_CUDA_ARCH_LIST=${_CUDA_ARCH_LIST} \
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
