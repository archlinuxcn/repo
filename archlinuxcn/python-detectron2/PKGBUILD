# Maintainer: Butui Hu <hot123tea123@gmail.com>

_CUDA_ARCH_LIST="5.2;5.3;6.0;6.1;6.2;7.0;7.2;7.5;8.0;8.6;8.6+PTX"
pkgname=(python-detectron2 python-detectron2-cuda)
_pkgname=detectron2
pkgver=0.6
pkgrel=4
pkgdesc="FAIR's next-generation platform for object detection and segmentation"
arch=('x86_64')
url='https://github.com/facebookresearch/detectron2'
license=('Apache')
depends=(
  python-cloudpickle
  python-future
  python-fvcore
  python-hydra-core
  python-iopath
  python-matplotlib
  python-mock
  python-omegaconf
  python-opencv
  python-pillow
  python-pycocotools
  python-pydot
  python-tabulate
  python-termcolor
  python-tqdm
  python-yacs
  tensorboard
)
makedepends=(
  cuda
  python-setuptools
  python-pytorch-cuda
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/facebookresearch/detectron2/archive/v${pkgver}.tar.gz")
sha256sums=('9757fed05fa32acc2116ea038185f08409d5e854573e70f41909a358b70d1004')

prepare() {
  cp -a "${_pkgname}-${pkgver}" "python-${_pkgname}-${pkgver}" 
  cp -a "${_pkgname}-${pkgver}" "python-${_pkgname}-cuda-${pkgver}" 
}

build() {
  cd "python-${_pkgname}-${pkgver}"
  python setup.py build

  cd "${srcdir}/python-${_pkgname}-cuda-${pkgver}"
  TORCH_CUDA_ARCH_LIST=${_CUDA_ARCH_LIST} \
  FORCE_CUDA=1 python setup.py build
}

package_python-detectron2() {
  depends+=(
    python-pytorch
  )
  cd "${pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}

package_python-detectron2-cuda() {
  pkgdesc="${pkgdesc} (with CUDA)"
  depends+=(
    cuda
    python-pytorch-cuda
  )
  provides=(python-detectron2=${pkgver})
  conflicts=(python-detectron2)
  cd "${pkgname}-${pkgver}"
  TORCH_CUDA_ARCH_LIST=${_CUDA_ARCH_LIST} \
  FORCE_CUDA=1 python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
# vim:set ts=2 sw=2 et:
