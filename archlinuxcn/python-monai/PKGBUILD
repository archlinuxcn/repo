# Maintainer: Butui Hu <hot123tea123@gmail.com>

_CUDA_ARCH_LIST="6.0;6.1;6.2;7.0;7.2;7.5;8.0;8.6;8.6;8.9;9.0;9.0+PTX"
pkgname=python-monai
_pkgname=MONAI
pkgver=1.3.0
pkgrel=2
pkgdesc='AI Toolkit for Healthcare Imaging'
arch=('x86_64')
url='https://monai.io'
license=('Apache-2.0')
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
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/Project-MONAI/MONAI/archive/refs/tags/${pkgver}.tar.gz"
        "0001-fix-building-torch-extension-with-glog.patch"
)
sha512sums=('757e96639d734fc031f8fa0bbd6399034c67930b9520cca02d0b0884b23c92de7e18eb3a1256aa210ed3a5cc1d4f53ef94ca9c2ca0626340acee380ff08cca88'
            '7096cc49314e366e60ce07e76709a6ccf13221cf95f01267a91ac5668e65935ede33eb28f957a561d16c5ff42f45a5b0bd65d869be0ef96f9ed61b9517157343')

prepare() {
  cd ${_pkgname}-${pkgver}
  patch -p1 -i ${srcdir}/0001-fix-building-torch-extension-with-glog.patch
}

build() {
  cd "${_pkgname}-${pkgver}"
  BUILD_MONAI=1 \
  FORCE_CUDA=1  \
  TORCH_CUDA_ARCH_LIST=${_CUDA_ARCH_LIST} \
  python -m build --wheel --no-isolation -x
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
}
# vim:set ts=2 sw=2 et:
