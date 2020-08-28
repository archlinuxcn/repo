# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-detectron2
_pkgname=detectron2
pkgver=0.2.1
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
  python-pytorch-cuda
  python-tabulate
  python-termcolor
  python-torchvision
  python-tqdm
  python-yacs
  tensorboard
)
optdepends=('opencv')
makedepends=(
  python-setuptools
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/facebookresearch/detectron2/archive/v0.2.1.tar.gz")
sha256sums=('ee3e404f534c03883423846876522d6b1e3e64796abd12caf51e8f8648bd5a63')

build() {
  cd "${_pkgname}-${pkgver}"
  FORCE_CUDA=1 python setup.py build
}


package() {
  cd "${_pkgname}-${pkgver}"
  FORCE_CUDA=1 python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
# vim:set ts=2 sw=2 et:
