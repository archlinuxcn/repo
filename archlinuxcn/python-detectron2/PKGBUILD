# Maintainer: Butui Hu <hot123tea123@gmail.com>

_CUDA_ARCH_LIST="5.2;5.3;6.0;6.1;6.2;7.0;7.0+PTX;7.2;7.2+PTX;7.5;7.5+PTX;8.0;8.0+PTX;8.6;8.6+PTX"
pkgname=(python-detectron2 python-detectron2-cuda)
_pkgname=detectron2
pkgver=0.5
pkgrel=1
pkgdesc="FAIR's next-generation platform for object detection and segmentation"
arch=('x86_64')
url='https://github.com/facebookresearch/detectron2'
license=('Apache')
depends=(
  python-cloudpickle
  python-future
  python-fvcore
  python-matplotlib
  python-mock
  python-pillow
  python-pycocotools
  python-pydot
  python-tabulate
  python-termcolor
  python-tqdm
  python-yacs
  tensorboard
)
optdepends=('opencv')
makedepends=(
  cuda
  python-setuptools
  python-pytorch-cuda
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/facebookresearch/detectron2/archive/v${pkgver}.tar.gz")
sha256sums=('eb5a63dc89face5f0ba8b9cd66283817f79afa0445937614af8225712274787f')

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
