# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=(python-detectron2 python-detectron2-cuda)
_pkgname=detectron2
pkgver=0.2.1
pkgrel=2
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
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/facebookresearch/detectron2/archive/v0.2.1.tar.gz")
sha256sums=('ee3e404f534c03883423846876522d6b1e3e64796abd12caf51e8f8648bd5a63')

prepare() {
  cp -a "${_pkgname}-${pkgver}" "python-${_pkgname}-${pkgver}" 
  cp -a "${_pkgname}-${pkgver}" "python-${_pkgname}-cuda-${pkgver}" 
}

build() {
  cd "python-${_pkgname}-${pkgver}"
  python setup.py build

  cd "${srcdir}/python-${_pkgname}-cuda-${pkgver}"
  TORCH_CUDA_ARCH_LIST="5.2;5.3;6.0;6.0+PTX;6.1;6.1+PTX;6.2;6.2+PTX;7.0;7.0+PTX;7.2;7.2+PTX;7.5;7.5+PTX;8.0;8.0+PTX" \
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
  cd "${pkgname}-${pkgver}"
  TORCH_CUDA_ARCH_LIST="5.2;5.3;6.0;6.0+PTX;6.1;6.1+PTX;6.2;6.2+PTX;7.0;7.0+PTX;7.2;7.2+PTX;7.5;7.5+PTX;8.0;8.0+PTX" \
  FORCE_CUDA=1 python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
# vim:set ts=2 sw=2 et:
