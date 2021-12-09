# Maintainer: Butui Hu <hot123tea123@gmail.com>

_CUDA_ARCH_LIST="5.2;5.3;6.0;6.1;6.2;7.0;7.0+PTX;7.2;7.2+PTX;7.5;7.5+PTX;8.0;8.0+PTX;8.6;8.6+PTX"
pkgname=python-monai
_pkgname=MONAI
pkgver=0.8.0
pkgrel=1
pkgdesc='Python wrap of crf and dense crf, both 2d and 3d are supported'
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
sha512sums=('054d1edb6a63fb2050ea7463d0134bebef993b34f37dd7b8555ed15bc47a57c41851a30b0ce1831fd9bf0397785c28ec02a6b8f22c891303da0c2348b664a18a')

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
