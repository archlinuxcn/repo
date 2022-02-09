# Maintainer: Butui Hu <hot123tea123@gmail.com>

_CUDA_ARCH_LIST="5.2;5.3;6.0;6.1;6.2;7.0;7.2;7.5;8.0;8.6;8.6+PTX"
pkgname=python-monai
_pkgname=MONAI
pkgver=0.8.1rc5
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
  python-pip
  python-setuptools
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
sha512sums=('f4695e05b612f6dfaa0db829f31671523cc467247d5cada96cdff154fdbdb860784099ed0d94fbfbc91993ff20e770631e138b8b0b8e52d2de707122fe051d8b')

build() {
  cd "${_pkgname}-${pkgver}"
  BUILD_MONAI=1 \
  FORCE_CUDA=1 \
  TORCH_CUDA_ARCH_LIST=${_CUDA_ARCH_LIST} \
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  BUILD_MONAI=1 \
  FORCE_CUDA=1 \
  TORCH_CUDA_ARCH_LIST=${_CUDA_ARCH_LIST} \
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
